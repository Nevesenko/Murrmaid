import json
import asyncio
import src.backend.notion_api as nback
import pandas as pd
import logging
from itertools import islice
import time
import requests

DB_ID = 'cb543354fca64e40b7554468b2ea3218'


jsonn = {"filter":{
    "and" : [
        {
            "property": "Formula_for_filtering_date",
            "number": {
                "less_than_or_equal_to" : 1719230040000

        }
        },
        {
            "property" : "Created time",
            "date": {
                "equals" : "2024-06-24"
            }
        }
    ]
}
}
# 1719230040000 2:54
# 1719235800000 4:30 вечера

def request_to_database():
    logging.critical("Делаем очередной запрос к БД")
    result = nback.parse_data(json = jsonn)
    res = result['results']
    lis = pd.json_normalize(res)['id'].tolist()
    logging.critical(f"Длина запроса : {len(lis)}")
    return lis, result["next_cursor"]

#можно сделать отдельный модуль для сформированной документации
count = 0

async def req(page, jsonn):
    logging.critical('Начал запрос')
    res = nback.update_page(page, jsonn)
    global count
    count += 1
    logging.critical(f'Запрос выполнен : {res.ok}, по счёту {count}')

async def main(lis_as):
    for page in lis_as:
        jsonn = {"archived": True}
        res = await req(page, jsonn)

def just_func(lis_just):
    count = 0
    for page in lis_just:
        jsonn =  {"archived": True}
        res = nback.update_page(page, jsonn)
        count += 1
        logging.critical(f'Запрос выполнен : {res.ok}, по счёту {count}')



# start = time.time()
# asyncio.run(main())
# end = time.time()
# asyncio_res = end - start
def all_arch():
    start = time.time()
    l, cursor = request_to_database()
    just_func(l)
    end = time.time()
    just_res = end - start
# print(f"Результат асинхронной программы: {asyncio_res}")
    print(f"Результат обычной программы: {just_res}")
    if cursor == None:
            return 'Done'
    return all_arch()

# r = requests.post('https://api.notion.com/v1/databases/4da56359021c418f9e9bc4e7e97bc9f9/query',
#               headers = nback.headers,
#               json = {"filter": {"property": "tg_id", "number": {"equals": 368} }})
#
# cursor = r.json()["next_cursor"]
# print(bool(cursor))
# print(type(cursor))

all_arch()