import json
from src.Конфиги.config import *
import requests




def add_new_user(message):
    with open(DATABASE_NAME, 'r') as f:
        data = json.load(f)
        isUserExist = bool(data.get(message.chat.id))
        if isUserExist:
            return True   # напечатать пользователю сообщение о том, что он уже зарегистрирован
        else:
            token = 'secret_sgke2SEfo1wuw0U4a6Zoi4W88830NoDMSXO4jDA4sKB' ####необходимо спросить у пользака токен и возможно объяснить как его получить
            page_id = "9d02837e3f8c4c8a92b162a2d95eaa50" #Ссылка на основную страницу
            auth_headers = {}
            body = {}
            body["parent"] = {
                "type": "page_id",
                "page_id": page_id
            }
            body["title"] = 'Main List'
            body['properties'] = { "Name": {
                    "title": {}
                } ,
            'tg_id' : {
                "number" : {}
            }}

            requests.post('', auth = auth_headers, json = body)
            return True #напечатать пользователю , что для него создана основная БД


class UserRequest:
    def __init__(self, message):
        chat_id = message.chat.id
        print(chat_id, type(chat_id))
        with open(DATABASE_NAME, 'r') as f:
            data = json.load(f)
            user_info = data[str(chat_id)]
        self.ID_DB_TEXT = user_info['textDatabaseId']
        self.ID_DB_CONNECTIONS = user_info['connectionsDatabaseId']
        self.ID_DB_PAGES = user_info['pagesDatabaseId']
        self.headers = {"Authorization": user_info['token'], "Notion-Version": NOTION_VERSION}



    def get__database_info(self):
        pass


    def query(self, attr, value, sorting = None, sort_filed = None):
        body = {}
        match attr:
            case 'tg_id':          #### сюда в планах дописать возможность вместо tg_id добавлять ещё что-то
                filter_properties = {
                    "property": "tg_id",
                    "number": {
                        "equals": value
                    }
                }
        body["filter"] = filter_properties

        if sorting is not None:
            body['sorts'] = {}  # дописать при необходимости иметь сортировку
        result = requests.post(f'https://api.notion.com/v1/databases/{self.ID_DB_TEXT}/query',
                               headers = self.headers, json = body )
        result = json.loads(result.text).get('results')
        return result

    def create_page(self, message):
        body = {
            "parent": {
                "database_id": self.ID_DB_TEXT
            },
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": message.text
                            }
                        }
                    ]
                }
            }
        }
        print(type(message))
        tg_id = message.id
        if tg_id:
            body['properties']['tg_id'] = {"number" : tg_id}

        result = requests.post('https://api.notion.com/v1/pages/', headers = self.headers, json = body )
        print(result.ok)
        result = json.loads(result.text)
        print('сделано')
        return result

    def create_connection(self, parent_id, child_id):
        body = {}
        body["parent"] =  {"database_id": self.ID_DB_CONNECTIONS}
        body["properties"] = {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "#####"
                        }
                    }
                ]
            } ,    # после пишем ссылку на нужные страницы
            "Parent" : {
                "relation": [
                    {
                      "id": parent_id
                    }
                  ]
                },
            "Child": {
                "relation": [
                    {
                        "id": child_id
                    }
                ]
            }
        }
        result = requests.post('https://api.notion.com/v1/pages/', headers = self.headers, json = body )
        result = json.loads(result.text).get('results')
        return result


    def update_page(self):
        pass