import json
import sqlite3


class UserDatabase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    full_name TEXT,
                    institution TEXT,
                    result TEXT
                )'''
        self.cursor.execute(query)
        self.connection.commit()

    def add_user(self, user_id, username):
        query = "INSERT INTO users (id, username) VALUES (?, ?)"
        try:
            self.cursor.execute(query, (user_id, username))
            self.connection.commit()
            print("Пользователь успешно добавлен в базу данных.")
        except sqlite3.Error as error:
            print("Ошибка при добавлении пользователя:", error)

    def add_result(self, user_id, result):
        query = "UPDATE users SET result = ? WHERE id = ?"
        try:
            # Преобразовываем словарь в JSON строку
            result_json = json.dumps(result)
            self.cursor.execute(query, (result_json, user_id))
            self.connection.commit()
            print("Результат пользователя успешно добавлен")
        except sqlite3.Error as error:
            print('Ошибка при добавлении результата пользователя:', error)

    def add_full_name(self, user_id, full_name):
        query = "UPDATE users SET full_name = ? WHERE id = ?"
        try:
            self.cursor.execute(query, (full_name, user_id))
            self.connection.commit()
            print("Полное имя пользователя успешно добавлено")
        except sqlite3.Error as error:
            print('Ошибка при добавлении полного имени пользователя:', error)

    def add_institution(self, user_id, institution):
        query = "UPDATE users SET institution = ? WHERE id = ?"
        try:
            self.cursor.execute(query, (institution, user_id))
            self.connection.commit()
            print("Учебное заведение пользователя успешно добавлено")
        except sqlite3.Error as error:
            print('Ошибка при добавлении учебного заведения пользователя:', error)
