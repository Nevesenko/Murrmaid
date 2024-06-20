#!/usr/bin/python
import requests
# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import telebot
import json
from src.Конфиги.config import *
import  logging
logging.basicConfig(level=logging.INFO)






def add_new_user(message):
    with open(DATABASE_NAME, 'r') as f:
        data = json.load(f)
    isUserExist = bool(data.get(message.chat.id))
    if isUserExist:
        return True  # напечатать пользователю сообщение о том, что он уже зарегистрирован
    else:
        pass