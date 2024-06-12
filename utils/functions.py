from utils.questions import questions_base


# Отправляет пользователю вопрос из списка
def send_questions(number: int):
    message = questions_base[number]
    return message["question"]
