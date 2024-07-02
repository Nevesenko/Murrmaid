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
    output = requests.post('cb543354fca64e40b7554468b2ea3218'.join(URL_DB_QUERY), headers=headers, json = json)
    logging.critical(f'Данные спрошены: {output.ok}' )
    res = output.json()  #написать try catch
    logging.debug(f"Джейсон раскрыт: {bool(res)}, тип : {type(res)}")
    return res


def add_note_to_db(db_id, json):
    res = requests.post('https://api.notion.com/v1/pages/',
                  headers = headers,
                  json = json)

    logging.critical(f'Строка добавлена: {res}')
    return res

def update_page(db_id, json):
    res = requests.patch('https://api.notion.com/v1/pages/' + db_id,
                         headers = headers,
                         json = json)
    logging.critical(f'Апдейт страницы произведен') #добавить подпись в виде айди странциы и имени бд
    return res
