from genericpath import exists
import json
from tokenize import String
from xml.etree.ElementTree import tostring
import openpyxl
import os
from loguru import logger
from xml_generation import generate_xml, generate_root, generate_head, generate_body, generate_b_part, generate_ending
from json_info import get_info_xlsx, get_info_xml
from excel import non_excise_groups_formulas, non_excise_dishes_formulas, list_excels, unmerge_cells, remove_rows_total, remove_rows_zero_price, add_formulas, get_date

excel_source_path = "./excel_source_path/"
excel_target_path = "./excel_target_path/"
xml_target_path = "./xml_target_path/"

date_cell = "A3"
restaurant_cell = "A6"
cooking_place_col = "B"
dishes_group_col = "C"
dishes_col = "D"
quantity_col = "E"
sum_col = "F"
sum_without_excise_col = "I"
sum_without_vat_col = "J"
price_col = "K"


def main():
    logger.info("### PROGRAM STARTED ###")
    # Work with config.json
    #hnum = input("Введіть номер з якого почати нумерувати податкові накладні: ")
    try:
        global config
        config = json.load(open("config.json", "r"))
    except Exception as e:
        logger.error("Config File does not exist. Please check!")
        logger.error(e)
        return
    # Get all files from directory
    logger.info("### EXCEL PART STARTED ###")
    try:
        excel_source_file = list_excels(excel_source_path)
    except Exception as e:
        logger.error(
            f"Error, source path {excel_source_path} not found. Current workid - {os.getcwd()}")
        logger.error(e)
        return
    for i in range(0, len(excel_source_file)):
        if excel_source_file[i].endswith(".xlsx"):
            try:
                wb = openpyxl.load_workbook(excel_source_file[i])
            except Exception as e:
                logger.error(f"Error opening {excel_source_file[i]} file")
                logger.error(e)
                return
            ws = wb.active
            unmerge_cells(ws)
            remove_rows_total(ws, cooking_place_col, dishes_group_col)
            remove_rows_zero_price(ws, sum_col)
            add_formulas(ws, sum_without_excise_col,
                         sum_without_vat_col, price_col, sum_col, quantity_col)
            iiko_name, non_excise_dishes, non_excise_groups = get_info_xlsx(
                ws, restaurant_cell, config)
            non_excise_dishes_formulas(ws, non_excise_dishes)
            non_excise_groups_formulas(ws, non_excise_groups)
            date = get_date(ws, date_cell)[0]
            if not os.path.exists(f"../{excel_target_path}"):
                os.makedirs(f"../{excel_target_path}")
            try:
                wb.save(f"../{excel_target_path}{date}_{iiko_name}.xlsx")
            except Exception as e:
                logger.error(
                    f"Error saving {excel_target_path}{date}_{iiko_name}.xlsx file")
                logger.error(e)
                return
            logger.info(f"File saved {excel_source_file[i]} file")
    logger.info("### EXCEL PART COMPLETED ###")

    input("Press Enter to continue...")

    logger.info("### XML PART STARTED ###")
    os.chdir("..")
    # For all target excels. Working with XML
    try:
        excel_target_file = list_excels(excel_target_path)
    except Exception as e:
        logger.error(
            f"Error, target path {excel_target_path} not found. Current workid - {os.getcwd()}")
        logger.error(e)
        return
    for i in range(0, len(excel_target_file)):
        if excel_source_file[i].endswith(".xlsx"):
            wb = openpyxl.load_workbook(excel_target_file[i], data_only=True)
            ws = wb.active
            iiko_name, hnamesel, tin, hksel, htinsel, hbos, hkbos = get_info_xml(
                ws, restaurant_cell, config)
            date, year, month = get_date(ws, date_cell)
            root = generate_root()
            generate_head(root, tin, period_month=month,
                          period_year=year, d_fill=date)
            declarbody = generate_body(root=root, hfill=date, hnamesel=hnamesel, hksel=hksel,
                                       htinsel=htinsel)
            row_num = 1
            for row in ws.iter_rows(min_row=6, max_row=ws.max_row):
                cell_row = str(row[0].row)
                dish = str(ws[f"{dishes_col}{cell_row}"].value)
                qnt = str(ws[f"{quantity_col}{cell_row}"].value)
                price = str(ws[f"{price_col}{cell_row}"].value)
                row_str = str(row_num)
                generate_b_part(declarbody, dish=dish,
                                row=row_str, qnt=qnt, price=price)
                row_num += 1
            generate_ending(declarbody, hbos=hbos, hkbos=hkbos)
            tree = generate_xml(root)
            if not os.path.exists(f"../{xml_target_path}"):
                os.makedirs(f"../{xml_target_path}")
            try:
                tree.write(f"../{xml_target_path}{date}_{iiko_name}.xml",
                           encoding="windows-1251", xml_declaration=True)
            except Exception as e:
                logger.error(
                    f"Error saving {xml_target_path}{date}_{iiko_name}.xml file")
                logger.error(e)
                return
    logger.info("### XML PART COMPLETED ###")

    logger.info("### PROGRAM COMPLETED ###")


if __name__ == "__main__":
    main()
