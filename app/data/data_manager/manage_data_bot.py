"""
File of data manager bot
Functions:
    - Manage site content from bot
"""

# Imports
import telebot
from config import Config

# Variables

bot = telebot.TeleBot(token=Config.token)


def is_admin(user_id: int) -> bool:
    """Function to check user is admin"""

    return user_id in Config.admins


@bot.message_handler(commands=['start'])
def start_command(message):
    """Start command handler"""

    if not is_admin(message.chat.id):
        bot.send_message(message.chat.id, 'You are not in admin list')
        return


bot.infinity_polling()
