import json
from tokenize import String
from xml.etree.ElementTree import tostring
import openpyxl
import os
import re
from loguru import logger

excel_source_path="/home/maksym/Maks/Projects/23-VAT-REPORT/excel_source_path/"
excel_target_path="/home/maksym/Maks/Projects/23-VAT-REPORT/excel_target_path/"
xml_source_path="/home/maksym/Maks/Projects/23-VAT-REPORT/xml_source_path/"
xml_target_path="/home/maksym/Maks/Projects/23-VAT-REPORT/xml_target_path/"
config=json.load(open("config.json","r"))

#Create functionality to add filepath manually
    #filePath = input('Please enter the path of the folder where the excel files are stored: ')
#Add check for overwriting
#Use col_range in remove rows func >>> col_range = ws['C:D']
#Write instruction for creating M5 report from IIKO


def main():
    logger.info("### PROGRAM STARTED ###")
    #List all files to var
    excel_source_file=list_excels(excel_path=excel_source_path)
    #For all files in dir
    for i in range(0, len(excel_source_file)):
        wb = openpyxl.load_workbook(excel_source_file[i])
        ws = wb.active
        unmerge_cells(ws)
        remove_rows_total(ws)
        add_formulas(ws)
        legal_name, non_excise_dishes, non_excise_groups = get_names(ws)
        non_excise_dishes_formulas(ws, non_excise_dishes)
        non_excise_groups_formulas(ws, non_excise_groups)
        date=get_date(ws)
        wb.save(excel_target_path+date+"_"+excel_source_file[i])
    logger.info("### EXCEL PART COMPLETED ###")   

    #For all target excels. Working with XML
    #excel_target_file=list_excels(excel_path=excel_target_path)
    #for i in range(0, len(excel_target_file)):
    #    wb = openpyxl.load_workbook(excel_target_file[i])
    #    ws = wb.active

    #logger.info("### XML PART COMPLETED ###") 

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
    #Removing rows with Total in "B" column - Місце приготування 
    for cell in ws['B']:
        if cell.value is not None:
            if "Total" in cell.value:
                ws.delete_rows(cell.row)
    #Removing rows with Total in "C" column - Група страви 
    for cell in ws['C']:
        if cell.value is not None:
            if "Total" in cell.value:
                ws.delete_rows(cell.row)

def add_formulas(ws):
    ws['I5'] = "Сума без акцизу"
    ws['J5'] = "Сума без ПДВ"
    ws['K5'] = "Ціна без ПДВ"
    
    #Start from D6
    for row in ws.iter_rows(min_col=4,max_col=4, min_row=6, max_row=ws.max_row):
        for cell in row:
            #Find price without excise
            ws[f'I{cell.row}'] = f"=F{cell.row}/105*100"
            #Find price without VAT
            ws[f'K{cell.row}'] = f"=I{cell.row}/6*5"
            #Find price for 1 product
            ws[f'J{cell.row}'] = f"=K{cell.row}/E{cell.row}"

#Non excise dishes check
def non_excise_dishes_formulas(ws, non_excise_dishes):
    counter=0
    for cell in ws['D']:
        if cell.value in non_excise_dishes:
            ws[f'I{cell.row}'] = f"=F{cell.row}"
            counter+=1
    logger.info(f"excise deleted for {counter} dishes")

#Non excise groups check
def non_excise_groups_formulas(ws, non_excise_groups):
    counter_groups=0
    counter_dishes=0
    for cell in ws['C']:
        if cell.value in non_excise_groups:
            ws[f'I{cell.row}'] = f"=F{cell.row}"
            counter_dishes+=1
            i=1
            while ws[f"C{cell.row+i}"].value==None:
                ws[f'I{cell.row}'] = f"=F{cell.row}"
                counter_dishes+=1
                i+=1
            counter_groups+=1
    logger.info(f"Excise deleted for {counter_dishes} dishes in {counter_groups} groups")


def get_names(ws):
    restaurant = ws['A6'].value
    if restaurant in config["legal_entities"]:
        iiko_name=config["legal_entities"][restaurant]["iiko_name"]
        legal_name=config["legal_entities"][restaurant]["legal_name"]
        non_excise_dishes=config["legal_entities"][restaurant]["non_excise_dishes"]
        non_excise_groups=config["legal_entities"][restaurant]["non_excise_groups"]
        logger.info(f"In restaurant {iiko_name} are: \nnon excise dishes - {non_excise_dishes} \nnon excise groups - {non_excise_groups}")
        return(legal_name, non_excise_dishes, non_excise_groups)
    else:
        logger.error(f"{ws['A6'].value} does not exist in JSON. Please check!")

def get_date(ws):
    #date to format ddmmyy
    date = re.sub("[^0-9]", "", ws['A3'].value)
    return date

if __name__ == "__main__":
    main()