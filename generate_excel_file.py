from genericpath import exists
import json
from tokenize import String
from xml.etree.ElementTree import tostring
import openpyxl
import os
from loguru import logger
from json_info import get_info_xlsx
import excel as ex
import get_database as gdb
import variables as var
from datetime import datetime


def main():
    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    logger.add(f"logs/excel-{time}.log")
    logger.info("### ПРОГРАМА РОЗПОЧАЛА РОБОТУ ###")
    excel_part()
    logger.info("### ПРОГРАМА ЗАКІНЧИЛА РОБОТУ ###")
    try:
        if "ERROR" in open(f"../logs/excel-{time}.log", "r").read():
            input(
                "При виконанні програми були помилочки. Перевір чи все гаразд \nНатисни Enter для виходу")
        else:
            input("Мені видається, що все пройшло добре. Натисни Enter для виходу")
    except Exception as e:
        logger.warning("Не вдалося перевірити чи були помилки при виконанні.")
        input("Натисни Enter для виходу")


def excel_part():
    # Work with config.json
    hnum = input("Введи номер, з якого почати нумерувати податкові накладні: ")
    while hnum.isdigit() == False:
        hnum = input(
            "От дідько :( Щось пішло не так\nВведи номер, з якого почати нумерувати податкові накладні: ")
    hnum = int(hnum)
    try:
        global config
        config = json.load(open("config.json", "r", encoding="utf-8"))
    except Exception as e:
        logger.error(
            "Схоже, що конфігураційного файлу не існує. Будь ласка. перевір!")
        logger.error(e)
        return
    # Get all files from directory
    logger.info("### ОБРОБКУ ЗВІТІВ З ФАЙЛІВ ЕКСЕЛЬ РОЗПОЧАТО ###")
    try:
        excel_source_file = ex.list_excels(var.excel_source_path)
    except Exception as e:
        logger.error(
            f"Помилка, шлях {var.excel_source_path} не знайдено. Поточна директорія - {os.getcwd()}")
        logger.error(e)
        return
    for i in range(0, len(excel_source_file)):
        if excel_source_file[i].endswith(".xlsx"):
            try:
                wb = openpyxl.load_workbook(excel_source_file[i])
            except Exception as e:
                logger.error(
                    f"Помилка відкривання файлу {excel_source_file[i]}")
                logger.error(e)
                return
            ws = wb.active
            # 1 - unmerge cells
            ex.unmerge_cells(ws)
            # remove delivery rows
            ex.remove_delivery(ws, var.payment_type_col)
            # clear columns
            ex.clear_cols(ws, var.cost_col, var.percent_col)
            # 2 - remove unused rows
            ex.remove_rows_total(ws, var.cooking_place_col,
                                 var.dishes_group_col)
            ex.remove_rows_zero_price(ws, var.sum_col)
            # add values
            try:
                ex.add_values(ws, var.dish_code_col, var.quantity_col, var.sum_col)
            except Exception as e:
                logger.error(
                    f"Помилка у модулі сумування страв")
                logger.error(e)
            # 3 - calculate without excise fromm all dishes
            try:
                ex.without_excise(ws, var.sum_without_excise_col, var.sum_col)
            except Exception as e:
                logger.error(
                    f"Помилка у модулі видалення акцизу")
                logger.error(e)
            # 4 -
            iiko_name, non_excise_dishes, non_excise_groups, db_name = get_info_xlsx(
                ws, var.restaurant_cell, config)
            # UKTZED
            dish_codes = ex.get_dish_codes(ws, var.dish_code_col)
            uktzed_codes = gdb.get_uktzed(
                dish_codes, db_name, config, var.place)
            if uktzed_codes != "None":
                ex.uktzed(ws, var.uktzed_col, uktzed_codes, var.dish_code_col)
            # 5 - check and recalculate excise
            ex.non_excise_dishes_formulas(
                ws, non_excise_dishes, var.sum_col, var.sum_without_excise_col, var.dishes_col)
            #ex.non_excise_groups_formulas(
            #    ws, non_excise_groups, var.sum_col, var.sum_without_excise_col, var.dishes_group_col)
            # 6 - put number of document
            ex.put_hnum(ws, var.document_text_cell,
                        var.document_number_cell, hnum)
            # 7 - calculate without VAT
            ex.without_vat(ws, var.sum_without_vat_col,
                           var.sum_without_excise_col)
            # 8 - calculate final price
            ex.price(ws, var.price_col,
                     var.sum_without_vat_col, var.quantity_col)
            ex.change_column_width(
                ws, var.sum_without_excise_col, var.sum_without_vat_col, var.price_col, var.uktzed_col)
            ex.get_total(ws, var.sum_without_excise_col,
                         var.sum_without_vat_col, var.sum_col)
            date = ex.get_date(ws, var.date_cell)[0]
            rest_dir_name = ex.get_dir_name(
                ws, var.restaurant_cell, var.cooking_place_cell)
            file_name = f"{var.excel_target_path}{rest_dir_name}/{date}_{iiko_name}.xlsx"
            if not os.path.exists(f"../{var.excel_target_path}{rest_dir_name}"):
                os.makedirs(f"../{var.excel_target_path}{rest_dir_name}")
            try:
                wb.save(f"../{file_name}")
            except Exception as e:
                logger.error(
                    f"Помилка збереження файлу {file_name}")
                logger.error(e)
                return
            logger.info(f"Файл збережено {file_name}")
            hnum += 1
    logger.info("### ОБРОБКУ ЗВІТІВ З ФАЙЛІВ ЕКСЕЛЬ ЗАВЕРШЕНО ###")


if __name__ == "__main__":
    main()
