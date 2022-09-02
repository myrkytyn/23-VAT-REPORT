from genericpath import exists
import json
from tokenize import String
from xml.etree.ElementTree import tostring
import openpyxl
import os
import re
from loguru import logger

excel_source_path = "./excel_source_path/"
excel_target_path = "./excel_target_path/"
xml_target_path = "./xml_target_path/"

restaurant_cell = "A6"
cooking_place = "B"
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
    except:
        logger.error("Config File does not exist. Please check!")
        return
    # Get all files from directory
    excel_source_file = list_excels(excel_source_path)
    for i in range(0, len(excel_source_file)):
        if excel_source_file[i].endswith(".xlsx"):
            try:
                wb = openpyxl.load_workbook(excel_source_file[i])
            except:
                logger.error(f"Error opening {excel_source_file[i]} file")
                return
            ws = wb.active
            unmerge_cells(ws)
            remove_rows_total(ws)
            remove_rows_zero_price(ws)
            add_formulas(ws)
            iiko_name, non_excise_dishes, non_excise_groups = get_info_xlsx(ws)
            non_excise_dishes_formulas(ws, non_excise_dishes)
            non_excise_groups_formulas(ws, non_excise_groups)
            date = get_date(ws)
            os.chdir("..")
            if not os.path.exists(excel_target_path):
                os.makedirs(excel_target_path)
            try:
                wb.save(f"{excel_target_path}{date}_{iiko_name}.xlsx")
            except:
                logger.error(f"Error saving {excel_source_file[i]} file")
                return
    logger.info("### EXCEL PART COMPLETED ###")

    # For all target excels. Working with XML
    # excel_target_file=list_excels(excel_path=excel_target_path)
    # for i in range(0, len(excel_target_file)):
    #    wb = openpyxl.load_workbook(excel_target_file[i])
    #    ws = wb.active

    # logger.info("### XML PART COMPLETED ###")

    logger.info("### PROGRAM COMPLETED ###")


def list_excels(excel_path):
    os.chdir(excel_path)
    excel_files = os.listdir('.')
    logger.info(f"In directory {excel_path} are files: \n{excel_files}")
    return excel_files


def unmerge_cells(ws):
    for merge in list(ws.merged_cells):
        ws.unmerge_cells(range_string=str(merge))


def remove_rows_total(ws):
    # Removing rows with Total in column - Місце приготування
    for cell in ws[cooking_place]:
        if cell.value is not None:
            if "Total" in cell.value:
                ws.delete_rows(cell.row)
    # Removing rows with Total in column - Група страви
    for cell in ws[dishes_group_col]:
        if cell.value is not None:
            if "Total" in cell.value:
                ws.delete_rows(cell.row)


def remove_rows_zero_price(ws):
    for cell in ws[sum_col]:
        if cell.value == 0:
            ws.delete_rows(cell.row)


def add_formulas(ws):
    ws[f"{sum_without_excise_col}5"] = "Сума без акцизу"
    ws[f"{sum_without_vat_col}5"] = "Сума без ПДВ"
    ws[f"{price_col}5"] = "Ціна без ПДВ"

    # Start from 6
    for row in ws.iter_rows(min_col=4, max_col=4, min_row=6, max_row=ws.max_row):
        for cell in row:
            # Find price without excise
            ws[f"{sum_without_excise_col}{cell.row}"] = f"={sum_col}{cell.row}/105*100"
            # Find price without VAT
            ws[f"{sum_without_vat_col}{cell.row}"] = f"={sum_without_excise_col}{cell.row}/6*5"
            # Find price for 1 product
            ws[f"{price_col}{cell.row}"] = f"={sum_without_vat_col}{cell.row}/{quantity_col}{cell.row}"


def non_excise_dishes_formulas(ws, non_excise_dishes):
    counter = 0
    for cell in ws['D']:
        if cell.value in non_excise_dishes:
            ws[f'I{cell.row}'] = f"=F{cell.row}"
            counter += 1
    logger.info(f"Excise deleted for {counter} dishes")


def non_excise_groups_formulas(ws, non_excise_groups):
    counter_groups = 0
    counter_dishes = 0
    for cell in ws['C']:
        if cell.value in non_excise_groups:
            ws[f'I{cell.row}'] = f"=F{cell.row}"
            counter_dishes += 1
            i = 1
            while ws[f"C{cell.row+i}"].value == None:
                ws[f'I{cell.row+i}'] = f"=F{cell.row+i}"
                counter_dishes += 1
                i += 1
            counter_groups += 1
    logger.info(
        f"Excise deleted for {counter_dishes} dishes in {counter_groups} groups")


def get_info_xlsx(ws):
    restaurant = ws[restaurant_cell].value
    if restaurant in config["legal_entities"]:
        iiko_name = config["legal_entities"][restaurant]["iiko_name"]
        non_excise_dishes = config["legal_entities"][restaurant]["non_excise_dishes"]
        non_excise_groups = config["legal_entities"][restaurant]["non_excise_groups"]
        logger.info(
            f"In restaurant {iiko_name} are: \nnon excise dishes - {non_excise_dishes} \nnon excise groups - {non_excise_groups}")
        return (iiko_name, non_excise_dishes, non_excise_groups)
    else:
        logger.error(f"{ws['A6'].value} does not exist in JSON. Please check!")


def get_date(ws):
    # date to format ddmmyyyy
    date = re.sub("[^0-9]", "", ws['A3'].value)
    return date


if __name__ == "__main__":
    main()
