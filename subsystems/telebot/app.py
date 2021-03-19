import logging

from telebot import TeleBot

from . import config, entities

# Настройка логирования
logging.basicConfig(
    #filename=config.LOG_PATH,
    level=logging.DEBUG,
)


# Инициализация сущностей бота
bot = TeleBot(
    token=config.TG_TOKEN,
    threaded=True,
    num_threads=2
)

# Импорт обработчиков команд


# Инициализация БД
entities.db.bind(provider='sqlite', filename=config.DB_PATH)
entities.db.generate_mapping()



