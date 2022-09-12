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
    logger.add("logs/file_{time}.log")
    logger.info("### PROGRAM STARTED ###")
    # Work with config.json
    #hnum = input("Введіть номер з якого почати нумерувати податкові накладні: ")
    try:
        global config
        config = json.load(open("config.json", "r", encoding="utf-8"))
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

    logger.info("### PROGRAM COMPLETED ###")

    input("Натисніть Enter для виходу з програми")


if __name__ == "__main__":
    main()
