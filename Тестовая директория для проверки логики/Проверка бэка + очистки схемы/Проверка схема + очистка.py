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
from src.cleaning.parsing_database_schema import *


def test_func():
    cur = backend.notion_api.parse_schema()
    logging.debug('Схема взята')
    exctract_properties_names(cur)
    logging.debug('Свойства взяты')
    return True

test_func()