import pypyodbc as db
from loguru import logger
import json_info as json


def get_uktzed(string_dishes, DATABASE, config, place, zero_uktzed):
    SERVER, UID, PASSWORD = json.get_info_db(config, place)
    logger.info(
        f"Розпочинаю витягувати коди УКТ ЗЕД з бази даних. Треба трохи зачекати")
    if zero_uktzed == None:
        zero_uktzed = '61D63FE7-212C-4847-BA32-1563D97E2424'
    try:
        conn = db.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};UID={UID};PWD={PASSWORD};DATABASE={DATABASE}")
    except Exception as e:
        logger.error(
            "Не можу з'єднатися з базою даних :(")
        logger.error(e)
        return "None"
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT m.c.value('(name/customValue/text())[1]', 'varchar(50)') as Dish,"
                        "CAST(outerEanCode.xml AS XML).query('r/outerEanCode').value('.', 'varchar(50)') as OuterEanCode"
                        f"FROM {DATABASE}.dbo.entity dish"
                        "CROSS APPLY (SELECT CAST(dish.xml as xml) as realxml) s"
                        f"CROSS APPLY s.realxml.nodes('r[type = \"DISH\"][num =({string_dishes})]') m(c)"
                        f"JOIN [{DATABASE}].[dbo].[entity] outerEanCode ON outerEanCode.id =  CAST(dish.xml AS XML).query('r/outerEconomicActivityNomenclatureCode').value('.', 'varchar(50)')"
                        "WHERE dish.type = 'Product'")
    except Exception as e:
        logger.error(
            "При виконанні запиту щось пішло не так")
        logger.error(e)
        return "None"
    uktzed_codes = cursor.fetchall()
    cursor.close()
    conn.close()
    logger.info(f"Роботу з базою даних завершено успішно!")
    return uktzed_codes


def get_item_name(num, DATABASE, config, place):
    SERVER, UID, PASSWORD = json.get_info_db(config, place)
    try:
        conn = db.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};UID={UID};PWD={PASSWORD};DATABASE={DATABASE}")
    except Exception as e:
        logger.error(
            "Не можу з'єднатися з базою даних :(")
        logger.error(e)
        return "None"
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT SUBSTRING(item_name.xml,(CHARINDEX('<customValue>', item_name.xml) + 13),(CHARINDEX('</customValue>', item_name.xml) - CHARINDEX('<customValue>', item_name.xml) - 13)) as 'Item' "
                       f"FROM [{DATABASE}].[dbo].[entity] dish "
                       f"JOIN [{DATABASE}].[dbo].[AssemblyChart] recipe ON recipe.product = dish.id "
                       f"JOIN [{DATABASE}].[dbo].[AssemblyChartItem] item ON item.assemblyChart_id = recipe.id "
                       f"JOIN [{DATABASE}].[dbo].[entity] item_name ON item_name.id = item.product "
                       f"WHERE dish.type = 'Product' "
                       f"AND SUBSTRING(dish.xml, (CHARINDEX('<num>', dish.xml) + 5), (CHARINDEX('</num>', dish.xml) - CHARINDEX('<num>', dish.xml) - 5))='{num}'")
    except Exception as e:
        logger.error(
            "При виконанні запиту щось пішло не так")
        logger.error(e)
        return "None"
    item_name = cursor.fetchall()
    cursor.close()
    conn.close()
    return item_name[0][0]
