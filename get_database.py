import pypyodbc as db
from loguru import logger
import json_info as json


def get_uktzed(string_dishes, DATABASE, config, place):
    SERVER, UID, PASSWORD = json.get_info_db(config, place)
    logger.info(
        f"Розпочинаю витягувати коди УКТ ЗЕД з бази даних. Треба трохи зачекати")
    uktzed_query = f"""SELECT m.c.value('(num/text())[1]', 'varchar(50)') as DishNumber,
    CAST(outerEanCode.xml AS XML).query('r/outerEanCode').value('.', 'varchar(50)') as OuterEanCode
    FROM {DATABASE}.dbo.entity dish
    CROSS APPLY (SELECT CAST(dish.xml as xml) as realxml) s
    CROSS APPLY s.realxml.nodes('r[type = \"DISH\"][num =({string_dishes})]') m(c)
    JOIN {DATABASE}.dbo.entity outerEanCode ON outerEanCode.id = m.c.value('(outerEconomicActivityNomenclatureCode/text())[1]', 'varchar(50)')
    WHERE dish.type = 'Product' AND dish.deleted = 0"""
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};UID={UID};PWD={PASSWORD};DATABASE={DATABASE}"
    try:
        conn = db.connect(connection_string)
    except Exception as e:
        logger.error(
            "Не можу з'єднатися з базою даних :(")
        logger.error(e)
        return "None"
    cursor = conn.cursor()
    try:
        cursor.execute(uktzed_query)
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
    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};UID={UID};PWD={PASSWORD};DATABASE={DATABASE}"
    try:
        conn = db.connect(connection_string)
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
