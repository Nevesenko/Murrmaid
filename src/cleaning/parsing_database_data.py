import logging
import json
import pandas as pd

def __extract_results(djson): #извлекает json содержащий results , т е тексты заметок
    print(11)
    res = djson.get('results')
    logging.debug(f"Получен список результата: {bool(res)}, {res}")
    return res

def get_metainfo(data : list): # извлекает
    meta = ["object", "id", "created_time", "last_edited_time", "cover", "icon", "parent" ]
    result = None
    try:
        result = pd.json_normalize(data)
    except Exception as e:
        print(e)
    return result