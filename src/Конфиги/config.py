
TOKEN = "Bearer secret_sgke2SEfo1wuw0U4a6Zoi4W88830NoDMSXO4jDA4sKB"
DATABASE_ID_TEXT = 'e99239d2cef746e6a2399c9946caade0' #все строки
DATABASE_ID_CONNECTIONS = '6224788771da49aca42899fdfec3a935' #все связи
DATABASE_ID_NETS = '1c635603bc7b4cffa1504bbd605988ec'  #перечисление всех страниц с отрисованными графами

DATABASE_NAME = 'База данных/text_db.json'
NOTION_VERSION = "2022-02-22"

USER_INFO = {'token' : None, "textDatabaseId" : None, "connectionsDatabaseId" : None, "pagesDatabaseId" : None}

DATABASE_FIELDS = {'Name':['title', 'text', 'content'],
                   'Text': ["rich_text"],
                   'Shape': ["select"],
                   'tg_id': ["number"]}

FILEDS = {"Status": "select", "tg_id" : "number"}


URL_DB_QUERY = ["https://api.notion.com/v1/databases/", "/query"]
URL_BLOCK_UPDATE = 'https://api.notion.com/v1/blocks/'
URL_NEW_PAGE = 'https://api.notion.com/v1/pages/'

CHUNK_SIZE = 1500