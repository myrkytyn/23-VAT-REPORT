from loguru import logger
import os
import re


def list_excels(excel_path):
    os.chdir(excel_path)
    excel_files = os.listdir('.')
    logger.info(f"В директорії {excel_path} є такі файли: \n{excel_files}")
    return excel_files


def unmerge_cells(ws):
    for merge in list(ws.merged_cells):
        ws.unmerge_cells(range_string=str(merge))


def remove_rows_total(ws, cooking_place_col, dishes_group_col):
    # Removing rows with Total in column - Місце приготування
    for cell in ws[cooking_place_col]:
        if cell.value is not None:
            if "Total" in cell.value or "всего" in cell.value:
                ws.delete_rows(cell.row)
    # Removing rows with Total in column - Група страви
    for cell in ws[dishes_group_col]:
        if cell.value is not None:
            if "Total" in cell.value or "всего" in cell.value:
                ws.delete_rows(cell.row)


def remove_rows_zero_price(ws, sum_col):
    for cell in ws[sum_col]:
        if cell.value == 0:
            ws.delete_rows(cell.row)


def add_formulas(ws, sum_without_excise_col, sum_without_vat_col, price_col, sum_col, quantity_col, uktzed_col):
    ws[f"{sum_without_excise_col}5"] = "Сума без акцизу"
    ws[f"{sum_without_vat_col}5"] = "Сума без ПДВ"
    ws[f"{price_col}5"] = "Ціна без ПДВ"
    ws[f"{uktzed_col}5"] = "Код УКТЗЕД"

    total_without_excise = 0
    total_without_vat = 0
    # Start from 6
    for row in ws.iter_rows(min_col=4, max_col=4, min_row=6, max_row=ws.max_row):
        for cell in row:
            # Find price without excise
            sum_without_excise_fl = round(
                float(ws[f"{sum_col}{cell.row}"].value)/105*100, 2)
            ws[f"{sum_without_excise_col}{cell.row}"] = str(
                sum_without_excise_fl)
            total_without_excise += sum_without_excise_fl
            # Find price without VAT
            sum_without_vat_fl = round((float(ws[f"{sum_without_excise_col}{cell.row}"].value)/6*5), 2)
            ws[f"{sum_without_vat_col}{cell.row}"] = str(sum_without_vat_fl)
            total_without_vat+=sum_without_vat_fl
            # Find price for 1 product
            ws[f"{price_col}{cell.row}"] = str(round((float(
                ws[f"{sum_without_vat_col}{cell.row}"].value)/float(ws[f"{quantity_col}{cell.row}"].value)), 2))
    ws[f"{sum_without_excise_col}{ws.max_row+1}"] = total_without_excise
    ws[f"{sum_without_vat_col}{ws.max_row}"] = total_without_vat


def non_excise_dishes_formulas(ws, non_excise_dishes, sum_col, sum_without_excise_col):
    counter = 0
    for cell in ws['D']:
        if cell.value in non_excise_dishes:
            ws[f"{sum_without_excise_col}{cell.row}"] = ws[f"{sum_col}{cell.row}"].value
            counter += 1
    logger.info(f"Акциз видалено з {counter} страв")


def non_excise_groups_formulas(ws, non_excise_groups, sum_col, sum_without_excise_col):
    counter_groups = 0
    counter_dishes = 0
    for cell in ws['C']:
        if cell.value in non_excise_groups:
            ws[f'{sum_without_excise_col}{cell.row}'] = ws[f"{sum_col}{cell.row}"].value
            counter_dishes += 1
            i = 1
            while ws[f"C{cell.row+i}"].value == None:
                ws[f'{sum_without_excise_col}{cell.row+i}'] = ws[f"{sum_col}{cell.row}"].value
                counter_dishes += 1
                i += 1
            counter_groups += 1
    logger.info(
        f"Акциз видалено з {counter_dishes} страв в {counter_groups} групах")


def get_date(ws, date_cell):
    # date to format ddmmyyyy
    date = re.sub("[^0-9]", "", ws[date_cell].value)
    year = date[-4:]
    if date[2] == "0":
        month = date[3]
    else:
        month = date[2]+date[3]
    return (date, year, month)


def get_dir_name(ws, restaurant_cell, cooking_place_cell):
    dir_suffix = ws[cooking_place_cell].value
    dir_suffix = dir_suffix[dir_suffix.find('ф'):]
    dir_name = f"{ws[restaurant_cell].value}-{dir_suffix}"
    return dir_name


def put_hnum(ws, text_cell, num_cell, hnum):
    ws[text_cell] = "Номер документу"
    ws[num_cell] = hnum


def change_column_width(ws, sum_without_excise_col, sum_without_vat_col, price_col, uktzed_col):
    ws.column_dimensions[sum_without_excise_col].width = 10
    ws.column_dimensions[sum_without_vat_col].width = 10
    ws.column_dimensions[price_col].width = 10
    ws.column_dimensions[uktzed_col].width = 20
    ws.column_dimensions["F"].width = 8
    ws.column_dimensions["G"].width = 8
    ws.column_dimensions["H"].width = 8
    ws.column_dimensions["I"].width = 8
