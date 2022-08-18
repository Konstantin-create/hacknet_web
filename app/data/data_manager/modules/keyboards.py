import telebot


def main_keyboard():
    """Markup for main menu"""

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        telebot.types.KeyboardButton(text='Index page')
    ]
    for btn in buttons:
        markup.add(btn)
    return markup


def init_page_keyboard():
    """Markup for index page items"""

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        telebot.types.KeyboardButton(text='Header Text'),
        telebot.types.KeyboardButton(text='About Text')
    ]
    for btn in buttons:
        markup.add(btn)

    return markup
