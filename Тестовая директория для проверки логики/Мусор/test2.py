from telebot import TeleBot, types

bot = TeleBot('7041392846:AAGa77iKT1BZYiZMZdv9lRysmjN73YFCU0s')


@bot.message_reaction_handler(reaction=types.MessageReactionCountUpdated)
def reaction_count_updated(update):
    message_id = update.message_id
    reactions = update.reactions
    print('2345678')
    # Обработать изменения в количестве реакций
    # ...

bot.polling()
