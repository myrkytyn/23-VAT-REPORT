import requests
import json_info as prop
from loguru import logger
import json
import hashlib


def main():
    try:
        global config
        config = json.load(open("config.json", "r", encoding="utf-8"))
    except Exception as e:
        logger.error(
            "Схоже, що конфігураційного файлу не існує. Будь ласка. перевір!")
        logger.error(e)
        return
    username, password = prop.get_info_api(config)
    pass_hash = hashlib.sha1(password.encode()).hexdigest()
    print (pass_hash)
    key = auth(username, pass_hash)
    response = generate_reports("21.10.2022","22.10.2022","12130d6c-7f79-4f14-a66b-1fe74f6a3727")
    print(response.status_code)
    print(response.text)

def auth(username, password):
    try:
        response = requests.get(f"http://iiko.23.ua:9080/resto/api/auth?login={username}&pass={password}")
    except Exception as e:
        logger.error(
            "Помилка в запиті авторизації")
        logger.error(e)
        return
    if response.status_code != 200:
        logger.error(
            f"Невдала авторизація. Статус код - {response.status_code}")
        return
    return 

def generate_reports(start_date, end_date, preset_id):
    response = requests.get(f"http://iiko.23.ua:9080/resto/service/reports/report.jspx?dateFrom={start_date}&dateTo={end_date}&presetId={preset_id}")
    return response

if __name__ == "__main__":
    main()

#http://iiko.23.ua:9080/resto/service/reports/report.jspx?dateFrom=22.10.2022&dateTo=22.10.2022&presetId=12130d6c-7f79-4f14-a66b-1fe74f6a3727

#if unautorize
#if 