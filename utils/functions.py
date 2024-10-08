from utils.questions import questions_base, description


# Отправляет пользователю вопрос из списка
def send_questions(number: int):
    message = questions_base[number - 1]
    return message["question"]


# Результат прохождения тестирования
def result(scores):
    combined_result = []
    # Сортируем словарь по значениям в порядке убывания
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Определяем максимальный балл
    max_score = sorted_scores[0][1]
    max_categories = [category for category, score in sorted_scores if score == max_score]
    additional_text = (f"Кейсы по {', '.join([description[cat].split('— ')[1].split(':')[0] for cat in max_categories])}"
                       f" мы скинем через 4 дня ❤️🔥")

    for i, (category, score) in enumerate(sorted_scores):
        if score == max_score and i == 0:
            combined_result.append("Лучшая совместимость🥰:")
        description_text = description[category]
        combined_result.append(f"<b><u>{score}/8</u></b> {description_text}")

    final_result = "\n\n".join(combined_result)
    return final_result, additional_text
