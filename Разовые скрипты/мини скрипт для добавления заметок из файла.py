import json

import src.backend.notion_api as nback
import pandas as pd
import logging
from itertools import islice
import time

DB_ID = 'cb543354fca64e40b7554468b2ea3218'


def read_file(path, begin = 26120 , end = 29768):
    table = pd.read_csv(path, sep='/', skip_blank_lines=True,  skiprows=lambda x: x<begin or x>end, names = ['Name', 'Transcription', 'Unit'] )
    return table
def form_the_note(info, db_id):
    body = {
        "parent": {
            "database_id": db_id
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": info.Name
                        }
                    }
                ]
            },
            "Unit": {
                "type" : "number",
                "number": int(info.Unit)
        },
            "Units_tags" : {
                "rich_text" : [{
                        "text" : {
                            "content" : info.Units_tags
                }
            }]

    }
    }}
    return body

def multiply_the_note(item):
    units = str(item['Unit']).strip().split(",")
    res = pd.DataFrame([])
    item['Units_tags'] = str(item['Unit']).strip()
    item['Name'] = ' ' if type(item['Name']) != str else item['Name']
    for i in units:
        cur = item.copy()
        cur['Unit'] = i.strip() if i.strip() != 'nan' and i.strip().isdigit()  else -1
        res = res._append(cur)
    return res

def main(path = 'C:\\Users\\a.nevesenko\\Downloads\\English Vocabulary in Use Upper-Intermediate 2017_orig.txt'):
    lines = read_file(path)

    for i in range(len(lines)):
        item = lines.iloc[i]
        prep_item = multiply_the_note(item)
        for row in prep_item.itertuples():
            logging.critical(f"Добавляем строку: {row}")
            body = form_the_note(row, db_id=DB_ID)
            nback.add_note_to_db(DB_ID, json = body)


# j = "{'Name': {'title': [{'text': {'content': 'admission'}}]}, 'Unit': {'type': 'text', 'text': {'content': '99'}}}".replace('\'', '\"')
# print(j)
# res = nback.add_note_to_db(DB_ID, j )
# print(res.ok)
# print(res)
main()