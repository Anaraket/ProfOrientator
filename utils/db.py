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
            self.cursor.execute(query, (result, user_id))
            self.connection.commit()
            print("Результат пользователя успешно добавлен")
        except sqlite3.Error as Error:
            print('Ошибка при добавлении результата пользователя:', Error)
