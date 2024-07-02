#!/usr/bin/python
import requests
# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import telebot
import json
from src.Конфиги.config import *
import  logging
logging.basicConfig(level=logging.INFO)
from src.Telegram_bot.tg_bot_worker import UserRequest
from src.Notion import notion_api_worker

API_TOKEN = '7041392846:AAGa77iKT1BZYiZMZdv9lRysmjN73YFCU0s'

isWaitingForSecret = None


class AdvancedTelebot(telebot.TeleBot):
    def managing(self):
        pass
processing = True
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['update'])
def draw_all_nodes(message):
    print('выполняю команду апдейт')
    app = notion_api_worker.Notion()
    app.update_mermaid_page("c433918fc1fc42a7897e723ffb3c0679")
    logging.info("Предупреждающее сообщение")
    @bot.message_handler(commands=['update'], func= lambda _: processing == True)
    def func(message):
        print('dyenhb')

# Handle '/start' and '/help'


@bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.send_message(message.chat_id, 'Привет. Зарегистрируй приложение и отправь мне код ')
#     bot.register_next_step_handler(message, save_the_secret)

def add_new_user(message):
    with open(DATABASE_NAME, 'r') as f:
        data = json.load(f)
        isUserExist = bool(data.get(message.chat.id))
        if isUserExist:
            return True  # напечатать пользователю сообщение о том, что он уже зарегистрирован
        else:
            token = 'secret_sgke2SEfo1wuw0U4a6Zoi4W88830NoDMSXO4jDA4sKB'  ####необходимо спросить у пользака токен и возможно объяснить как его получить
            page_id = "9d02837e3f8c4c8a92b162a2d95eaa50"  # Ссылка на основную страницу
            auth_headers__ = {"Authorization": TOKEN, "Notion-Version": NOTION_VERSION}
            body = {}
            body["parent"] = {"type": "page_id","page_id": page_id}
            body["title"] =  [{"type": "text", "text": {"content": "Main list"}}]
            body["properties"] = {"Name": {"title": {} },"tg_id": {"number": {}}}
            body_str = json.dumps(body).replace('\'', '\"')
            print(body_str)
            result_textbd = requests.post('https://api.notion.com/v1/databases/', headers=auth_headers__, json=body)
            print(result_textbd)
            txtId = json.loads(result_textbd.text)['id']
            # напечатать пользователю , что для него создана основная БД
    with open(DATABASE_NAME, 'w') as f:
        data[message.chat.id] =  {'token' : token, "textDatabaseId" : txtId , "connectionsDatabaseId" : None, "pagesDatabaseId": None }
        json.dump(data, f)


def save_the_secret(message):
    secret = message.text
    with open(DATABASE_NAME, 'a+') as f:
        data = json.load(f)
        user_info = data.chat_id


@bot.message_handler(func = lambda message: isWaitingForSecret)
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.edited_message_handler()
def func(call):
    print('Печатаем call : ', call)


@bot.message_handler(func=lambda message: message.reply_to_message is not None)
def create_connection(message):
    user = UserRequest(message)
    parent_tg_id = message.reply_to_message.id
    # создаем запрос на поиск parent - message в БД test
    result = user.query('tg_id', parent_tg_id)
    idOfTheParent = result[0]["id"]
    #создаем новую заметку
    new_page = user.create_page(message)
    idOfNewPage = new_page['id']
    #создаем связь -- обращаемся к БД  для связей
    user.create_connection(parent_id = idOfTheParent, child_id = idOfNewPage)


@bot.message_handler(func=lambda message: True)
# def saving_text(message):
    # new_node = message.text
    # print(solution_class.app.save_new_node(new_node))
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn2 = types.KeyboardButton("Что я могу?")
    # markup.add(btn2)
def save_note(message):
    print(message)
    print(message.chat.id)
    #print(json.dumps(message.__str__(), indent=4))
    user = UserRequest(message)
    user.create_page(message)
    print('Просто проверка сообщения', message)

    #bot.send_message(message.chat.id,'Тест' ,reply_markup=markup)

@bot.poll_answer_handler()
def handle_poll_answer(pollAnswer):
    print(pollAnswer)

@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    print(message)
@bot.message_reaction_handler(func=lambda call: True)
def handle_callback_query(call):
    print(call)
    print('Внутри декоратора, реагирующего реакции')



bot.infinity_polling()