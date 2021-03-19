from queue import Queue
from typing import NamedTuple, Callable
from datetime import datetime


class OnTimeTask(NamedTuple):
    """
    Задача, выполняемая главным процессом после наступление заданного помента времени
    datetime - момент времени, после которого задача должна быть выполнена
    target_func - функция, которую нужно выполнить
    args, kwargs - аргументы, передаваемые фунции target_func
    """
    target_func: Callable
    args: tuple
    kwargs: dict
    datetime: datetime


def perform_on_time_tasks(tasks_list: list[OnTimeTask], time_now: datetime) -> None:
    """Выполняет задачи, если их время пришло"""
    tasks_to_perform = [task for task in tasks_list if task.datetime < time_now]
    for task in tasks_to_perform:
        task.target_func(*task.args, **task.kwargs)
        tasks_list.remove(task)
