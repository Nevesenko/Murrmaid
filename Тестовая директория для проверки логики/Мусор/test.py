import pandas as pd
import requests
import json
DATABASE_ID = 'e99239d2cef746e6a2399c9946caade0'


url_ = f'https://api.notion.com/v1/databases/{DATABASE_ID}'
url_database_info = 'https://api.notion.com/v1/databases/e99239d2cef746e6a2399c9946caade0'
url_create_page = 'https://api.notion.com/v1/pages/'
body_create_page_postman = {
    "parent": {
        "database_id": "e99239d2cef746e6a2399c9946caade0"
    },
    "properties": {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "New Media Article"
                    }
                }
            ]
        },
        "tg_id": {
            "number": 42
        }
    }
}
body_create_page = {
    "parent": {
        "database_id": DATABASE_ID
    },
    "properties": {
        
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "New Media Article"
                    }
                }
            ]
        },
        "Status": {
            "select": {
                "id": "8c4a056e-6709-4dd1-ba58-d34d9480855a",
                "name": "Done"
            }
        }
    }
}

token = 'secret_sgke2SEfo1wuw0U4a6Zoi4W88830NoDMSXO4jDA4sKB'
headers = {"Authorization": f"Bearer {token}","Notion-Version":"2022-02-22"}



result  = requests.post(url=url_create_page, headers=headers, json = body_create_page_postman)
print(result)