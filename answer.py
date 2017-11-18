
ANSWER = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

def get_answer(question, answer):
    question_lower = question.lower()
    if question_lower in answer:
        return answer[question_lower]

print(get_answer('Привет', ANSWER))