from multiprocessing.connection import Connection
from .app import bot


def main(conn: Connection):
    bot.polling()


if __name__ == '__main__':
    bot.polling()
