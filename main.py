import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.reply_to(message, pokemon.info())
        bot.reply_to(message, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")




@bot.message_handler(func=lambda message: True, content_types=['sticker','photo'])
def handle_sticker(msg):
    chat_id = msg.chat.id # сохранение id чата
    user_id = msg.from_user.id
    bot.ban_chat_member(chat_id, user_id)
    bot.delete_message(msg.chat.id, msg.message_id)


bot.infinity_polling(none_stop=True)

