import sqlite3
from typing import Optional, List, Tuple


class Database:
    def __init__(self, db_path: str) -> None:
        """Инициализация соединения с базой данных."""
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self) -> None:
        """Создание таблиц для пользователей и задач."""
        cursor: sqlite3.Cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            status INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """)
        self.conn.commit()

    def add_user(self, user_id: int, username: str, name: str) -> None:
        """Добавление нового пользователя в базу данных."""
        cursor: sqlite3.Cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (user_id, username, name) VALUES (?, ?, ?)", (user_id, username, name))
        self.conn.commit()

    def get_user(self, username: str) -> Optional[Tuple[int, int, str, str]]:
        """Получение пользователя по его логину."""
        cursor: sqlite3.Cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user: Optional[Tuple[int, int, str, str]] = cursor.fetchone()
        return user

    def add_task(self, user_id: int, title: str, description: str, status: int) -> None:
        """Добавление новой задачи для пользователя."""
        cursor: sqlite3.Cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (user_id, title, description, status) VALUES (?, ?, ?, ?)",
            (user_id, title, description, status)
        )
        self.conn.commit()

    def get_tasks(self, user_id: int) -> List[Tuple[int, int, str, str, int]]:
        """Получение всех задач пользователя."""
        cursor: sqlite3.Cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        tasks: List[Tuple[int, int, str, str, int]] = cursor.fetchall()
        return tasks

    def update_task_status(self, task_id: int, status: int) -> None:
        """Обновление статуса задачи."""
        cursor: sqlite3.Cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        self.conn.commit()

    def delete_task(self, task_id: int) -> None:
        """Удаление задачи по её идентификатору."""
        cursor: sqlite3.Cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
