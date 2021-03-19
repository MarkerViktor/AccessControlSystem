from multiprocessing import Process
from multiprocessing import Pipe

from multiprocessing.connection import Connection
from collections import Callable

from json import dumps, loads


class Subsystem:
    """Базовый класс процессов-подсистем СКД"""

    def __init__(self,
                 name: str,
                 entry_point: Callable[[Connection], None],
                 server_conn: Connection,
                 subsystem_conn: Connection):
        """
        name - имя подсистемы,
        entry_point - точка входа подсистемы,
        server_conn - объект соединения, через который главный процесс будет общаться с подсистемой
        subsystem_conn - объект соединения, через который подсистема будет общаться с главным процессом
        """
        self.name = name
        self._server_conn = server_conn
        self._entry_point = entry_point
        self.process = Process(name=name, target=entry_point, args=(subsystem_conn,))

    def send(self, data: dict or list):
        """Отправить сообщение процессу"""
        self._server_conn.send_bytes(dumps(data).encode('utf-8'))

    def recv(self) -> dict or list:
        """Получить сообщение от процесса"""
        data = self._server_conn.recv_bytes().decode('utg-8')
        return loads(data)

    def poll(self):
        """Получены ли сообщения от подсистемы"""
        return self._server_conn.poll()

    def start_process(self):
        """Запуск процесса подсистемы"""
        self.process.start()


def make_subsystem(name: str, entry_point: Callable[[Connection], None], duplex=True) -> Subsystem:
    """Создает экземпляр класса Subsystem с новыми объектами Connections"""
    server_conn, subsystem_conn = Pipe(duplex=duplex)
    return Subsystem(name, entry_point, server_conn, subsystem_conn)

