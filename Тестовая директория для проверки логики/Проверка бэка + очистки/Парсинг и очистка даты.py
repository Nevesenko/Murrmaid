from src.Конфиги.config import *
import logging
import json
import pandas as pd
##############################################

import src.backend.notion_api as backend_requests

logging.basicConfig(level=logging.DEBUG)
headers = {"Authorization": TOKEN, "Notion-Version": "2022-02-22"} #это будет выноситься в запросы к БД



import src.backend as backend
import src.cleaning as cleaning
from src.cleaning.parsing_database_data import __extract_results, get_metainfo
def test_func():
    try:
        cur = backend.notion_api.parse_data()
        logging.debug(f"Запрос к бэку выполнен: {bool(cur)}")
        print(1)
        cur = __extract_results(cur)
        logging.debug(f"Очистка выполнена: {bool(cur)}")   #чтобы это нормально работало, надо записать try-catch теле функции
        cur = get_metainfo(cur)
        cur.to_csv('Эксель с очищенными данными.csv')
        logging.debug(f"Извлечение данных выполнено")
    except Exception as e:
        raise e
    return True


logging.debug(test_func())