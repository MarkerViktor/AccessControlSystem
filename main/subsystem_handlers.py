from threading import Thread
from typing import Callable

from main import hardware_commands
from main import telebot_commands
from main.tasks import Tasks
from subsystems import Subsystem


def face_id_handler(request: dict or list, tasks: Tasks, subsystem: Subsystem) -> dict or list or None:
    """Обработчки событий (сообщенией), вызываемых подсистемой аутентификации"""
    room_id = request['room_id']
    is_known = request['is_known']

    if is_known:
        # Обнаружен известный пользователь
        user_id = request['user_id']
        hardware_commands.open_door(user_id, room_id)
        return {'status': 'OK'}
        # TODO: Добавить обработку исключений при невозможности открытия помещения
    else:
        # Обнаружен неизвестный пользователь
        similar_ids = {user['id']: user['prob'] for user in request['similar_ids']}
        img_path = request['img_path']

        def ask_admins_in_background_func(room_id: int, img_path: str,
                                          similar_ids: dict[int, float], send_answer_func):
            """Функция, запускаемая в отдельном потоке, """

        # Совершаем опрос администраторов в отдельном потоке
        Thread(target=_face_id_ask_admins, args=(room_id, img_path, similar_ids, subsystem.send)).start()
        return None
        # Ответ будет отправлен позже


def hardware_handler(request: dict or list, tasks: Tasks, subsystem: Subsystem) -> dict or list:
    pass


def telebot_handler(request: dict or list, tasks: Tasks, subsystem: Subsystem) -> dict or list:
    pass
