import requests
import json

from src.Конфиги.config import *
class Notion:

    def __init__(self, database_id = None):
        self.db = database_id
        self.chat_id = None
        self.headers = {"Authorization": TOKEN, "Notion-Version": "2022-02-22"}

    def draw_mermaid_graph(self):
    #Делает запрос к БД, извлекает все ноды,
        print('Делаю запрос внутри функции draw_mermaid_graph')
        #прописываем создание фильтра

        filt = {}
        # result = requests.post(DATABASE_ID_TEXT.join(URL_DB_QUERY), headers=self.headers)

        def make_query(db_id, parameter):
            res = None
            match parameter:
                case 'retrive':
                    result = requests.get(db_id.join(URL_DB_QUERY[0]), headers=self.headers)
                    res = json.loads(result.text).get('properties')
                case 'query':
                    result =  requests.post(db_id.join(URL_DB_QUERY), headers=self.headers)
                    res = json.loads(result.text).get('results')
            return res

        def return_name_property(item):
            textt =  item['properties']['Name']["title"]
            if textt == []:
                return 'no value'
            else:
                return textt[0]["text"]["content"]

        def wrap_the_text(text_block):
            shapes = {'square': ('[', ']'),
                     'round' : ('(',')') }
            first, last = shapes['round']
            text_block = text_block.replace("\"", "\'")
            return first + "\"" + text_block + "\"" + last

        info_about = make_query(DATABASE_ID_TEXT, 'query')
        data = make_query(DATABASE_ID_TEXT, 'query')
        print('Сделан запрос на чтение всех заметок')
        str_nodes = ''
        for item in data:
            textOfNode = wrap_the_text(return_name_property(item))
            str_nodes += ''.join([item["id"], textOfNode, '\n', ])

        result = requests.post(DATABASE_ID_CONNECTIONS.join(URL_DB_QUERY), headers=self.headers)
        data = json.loads(result.text).get('results')

        data = make_query(DATABASE_ID_CONNECTIONS)
        for item in data:
            parent = item['properties']['Parent']['relation'][0]['id']
            child = item['properties']['Child']['relation'][0]['id']
            new_connection = parent + ' --> ' + child
            str_nodes += new_connection + '\n'
        return str_nodes

    def update_mermaid_page(self, page_id, orientation : str = 'LR'):
        code_str = self.draw_mermaid_graph()
        chunks = len(code_str) // CHUNK_SIZE ## 1500
        body_text = []
        def add_new_values_to_graph(new_notion_text):
            block_for_appending = {"type": "text","text": {} }
            block_for_appending["text"]["content"]= new_notion_text
            return block_for_appending
        body_text.append(add_new_values_to_graph(f'graph {orientation} \n'))
        for i in range(chunks):
            body_text.append(add_new_values_to_graph(f'{code_str[i*CHUNK_SIZE : i*CHUNK_SIZE+CHUNK_SIZE]}'))
        body_text.append(add_new_values_to_graph(f'{code_str[chunks*CHUNK_SIZE::]}'))
        body = {"code": {"rich_text" : body_text , "language" : "mermaid" } }
        res = requests.patch(URL_BLOCK_UPDATE + '4e778fc264d64b6ab58dfed037fbdf3a', headers=self.headers, json = body)
        print('Result : ', res)
####

    def save_new_node(self, new_text, tg_id = 456):
        properties = { "Name": { "title": [ { "text" : { "content" : new_text } } ] } }
        if tg_id is not None:
            properties['tg_id'] =  {"number": tg_id}
        node_schema = {"parent": {"database_id": DATABASE_ID_TEXT},"properties" : properties}
        res = requests.post(URL_NEW_PAGE, headers=self.headers, json = node_schema)
        print(res)
        return res

# app = Notion(database_id='e99239d2cef746e6a2399c9946caade0')
#
# app.update_mermaid_page("c433918fc1fc42a7897e723ffb3c0679")
