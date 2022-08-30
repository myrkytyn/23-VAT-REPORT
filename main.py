import json
from tokenize import String
from xml.etree.ElementTree import tostring
import openpyxl
import os
import sys
import re

excel_source_path="/home/maksym/Maks/Projects/23-VAT-REPORT/excel_source_path/"
excel_target_path="/home/maksym/Maks/Projects/23-VAT-REPORT/excel_target_path/"
xml_source_path="/home/maksym/Maks/Projects/23-VAT-REPORT/xml_source_path/"
xml_target_path="/home/maksym/Maks/Projects/23-VAT-REPORT/xml_target_path/"
config=json.load(open("config.json","r"))

#Create functionality to add filepath manually
    #filePath = input('Please enter the path of the folder where the excel files are stored: ')
#Add перевірку на перезапис
#Use col_range in remove rows func >>> col_range = ws['C:D']
#Add Coffee logic (not use accise)
#Add logic with legal entities (Fabbrica, Delikacia)
#Write instruction for creating M5 report from IIKO


def main():
    print("### PROGRAM STARTED ###\n")
    #List all files to var
    excel_source_file=list_excels(excel_path=excel_source_path)
    #For all files in dir
    for i in range(0, len(excel_source_file)):
        wb = openpyxl.load_workbook(excel_source_file[i])
        ws = wb.active
        unmerge_cells(ws)
        remove_rows_total(ws)
        add_formulas(ws)
        get_names(ws)
        date=get_date(ws)
        wb.save(excel_target_path+date+"_"+excel_source_file[i])
    print("\n### EXCEL PART COMPLETED ###")   

    #For all target excels. Working with XML
    excel_target_file=list_excels(excel_path=excel_target_path)
    for i in range(0, len(excel_target_file)):
        wb = openpyxl.load_workbook(excel_target_file[i])
        ws = wb.active

    print("\n### XML PART COMPLETED ###") 

    print("\n### COMPLETED ###")                

def list_excels(excel_path):
    os.chdir(excel_path)
    excel_files = os.listdir('.')
    print(f"In directory {excel_path} there are files:")
    print(*excel_files, sep = "\n")
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
#def non_excise_dishes_formulas(ws,):
#    for cell in ws['D']:
#        if cell.value == :
#            ws[f'I{cell.row}'] = f"=F{cell.row}"

#Non excise groups check
#def non_excise_dishes_formulas(ws):
#    for column in ws.iter_columns():
#        for cell in column:

def get_names(ws):
    if ws['A6'].value == "Делікація Незалежності":
        restaurant="Delikacia"
        iiko_name=config["legal_entities"][restaurant]["iiko_name"]
        legal_name=config["legal_entities"][restaurant]["legal_name"]
        print(iiko_name,legal_name)

def get_date(ws):
    date = re.sub("[^0-9]", "", ws['A3'].value)
    return date

if __name__ == "__main__":
    main()