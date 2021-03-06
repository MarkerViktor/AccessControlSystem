from telebot.types import Message

from ..app import bot


@bot.message_handler(commands=['help', 'start'])
def bot_help(message: Message):
    """Справочная информация о командах"""
    help_text = '<b>Подробнее о командах:</b>'
    bot.send_message(chat_id=message.chat.id, text=help_text, parse_mode='HTML')
