"""
File of data manager bot
Functions:
    - Manage site content from bot
"""

# Imports
import telebot
from config import Config
from modules.keyboards import *

# Variables

bot = telebot.TeleBot(token=Config.token)


def is_admin(user_id: int) -> bool:
    """Function to check user is admin"""

    return user_id in Config.admins


@bot.message_handler(commands=['start'])
def start_handler(message):
    """Start command handler"""

    if not is_admin(message.chat.id):
        bot.send_message(message.chat.id, 'You are not in admin list')
        return
    bot.reply_to(message, 'Welcome to HackNet web panel. Choose menu option', reply_markup=main_keyboard())


@bot.message_handler(content_types=['text'])
def text_handler(message):
    """Function for handling text messages"""

    bot.delete_message(message.chat.id, message.id - 1)
    bot.delete_message(message.chat.id, message.id)
    if message.text.lower() == 'index page':
        bot.send_message(message.chat.id, 'Select element to manage', reply_markup=init_page_keyboard())

    elif message.text.lower() == 'header text':
        bot.send_message(message.chat.id, 'Current header text is: {}')


bot.infinity_polling()
