from typing import Callable, NamedTuple


class AskAdminsResult(NamedTuple):
    is_known: bool
    user_id: int


def ask_admins(room_id: int, img_path: str, similar_ids: dict[int, float]) -> AskAdminsResult:
    """Спросить администраторов указанного помещения о неизвестном пользователе"""
    return AskAdminsResult(is_known=True, user_id=1)
