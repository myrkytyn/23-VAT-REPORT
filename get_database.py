import pypyodbc as db
from loguru import logger
import json_info as json


def get_uktzed(string_dishes, DATABASE, config, place):
    SERVER, UID, PASSWORD = json.get_info_db(config, place)
    logger.info(f"Розпочинаю роботу з базою даних. Треба трохи зачекати")
    try:    
            conn = db.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};UID={UID};PWD={PASSWORD};DATABASE={DATABASE}")
    except Exception as e:
        logger.error(
            "Не можу з'єднатися з базою даних :(")
        logger.error(e)
        return "None"
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT SUBSTRING( dish.xml, (CHARINDEX('<num>', dish.xml) + 5), ( CHARINDEX('</num>', dish.xml) - CHARINDEX('<num>', dish.xml) - 5 ) ) as 'dish_number', "\
            "SUBSTRING( outerEanCode.xml, ( CHARINDEX('<outerEanCode>', outerEanCode.xml) + 14 ), ( CHARINDEX('</outerEanCode>', outerEanCode.xml) - CHARINDEX('<outerEanCode>', outerEanCode.xml) - 14 ) ) as 'OuterEanCode' "\
            f"FROM [{DATABASE}].[dbo].[entity] dish JOIN [{DATABASE}].[dbo].[entity] outerEanCode "\
            "ON outerEanCode.id = CASE WHEN CHARINDEX( '<outerEconomicActivityNomenclatureCode>', dish.xml ) > 0 THEN "\
            "SUBSTRING( dish.xml, ( CHARINDEX( '<outerEconomicActivityNomenclatureCode>', dish.xml ) + 39 ), ( CHARINDEX( '</outerEconomicActivityNomenclatureCode>', dish.xml ) - CHARINDEX( '<outerEconomicActivityNomenclatureCode>', dish.xml ) - 39 ) ) "\
            "ELSE '61D63FE7-212C-4847-BA32-1563D97E2424' END "
            "WHERE dish.type = 'Product' AND dish.deleted = 0 AND "\
            f"SUBSTRING( dish.xml, (CHARINDEX('<num>', dish.xml) + 5), ( CHARINDEX('</num>', dish.xml) - CHARINDEX('<num>', dish.xml) - 5 ) ) IN ({string_dishes})")
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