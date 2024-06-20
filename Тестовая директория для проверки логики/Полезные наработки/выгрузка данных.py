from src.Конфиги.config import *
import logging
import json
##############################################

import src.backend.notion_api as backend_requests

logging.basicConfig(level=logging.DEBUG)
headers = {"Authorization": TOKEN, "Notion-Version": "2022-02-22"} #это будет выноситься в запросы к БД


#как именно сокрыть логику запроса, если необходио добавить запрос с параметром/партицией
def clean_json(djson):
    logging.info('Начал парсинг схемы')
    keys = djson.keys()
    logging.debug(keys)
    return keys

def create_dict(s):
    res = json.loads(s.text).get('properties')
    logging.debug('Извлек категории из json')
    return res


schema = backend_requests.parse_schema()
cur = create_dict(schema)
cur = clean_json(cur)
