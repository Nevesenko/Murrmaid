import requests
from src.Конфиги.config import *
import logging



headers = {"Authorization": TOKEN, "Notion-Version": "2022-02-22"} #это будет выноситься в запросы к БД


def parse_schema():
    schema = requests.get(URL_DB_QUERY[0] + DATABASE_ID_TEXT, headers=headers)
    logging.info('Схема таблицы текстовых заметок загружена')
    logging.debug(type(schema))
    return schema.json()
def parse_data(json = None):
    output = requests.post(DATABASE_ID_TEXT.join(URL_DB_QUERY), headers=headers, json = json)
    logging.critical('Данные спрошены')
    res = output.json()  #написать try catch
    logging.debug(f"Джейсон раскрыт: {bool(res)}, тип : {type(res)}")
    return res
