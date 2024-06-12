from utils.questions import questions_base, description


# Отправляет пользователю вопрос из списка
def send_questions(number: int):
    message = questions_base[number - 1]
    return message["question"]


# Результат прохождения тестирования
def result(scores):
    combined_result = []
    for category, score in scores.items():
        combined_result.append(f"<b><u>{score}/8</u></b> {description[category]}")
    final_result = "\n\n".join(combined_result)
    return final_result
