from typing import Dict


class FSM:
    def __init__(self) -> None:
        """Инициализация состояния FSM для каждого пользователя."""
        self.states: Dict[int, str] = {}
        self.data: Dict[str, str] = {}

    def set_state(self, user_id: int, state: str) -> None:
        """Установка состояния для пользователя."""
        self.states[user_id] = state

    def get_state(self, user_id: int) -> str:
        """Получение текущего состояния пользователя."""
        return self.states.get(user_id)

    def reset_state(self, user_id: int) -> None:
        """Сброс состояния пользователя."""
        if user_id in self.states:
            del self.states[user_id]
