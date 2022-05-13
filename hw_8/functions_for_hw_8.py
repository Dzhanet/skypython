import json


def load_questions():
    """Загружаем вопросы из list_of_instances_of_class_Question.json"""

    file = open("list_of_instances_of_class_Question.json")
    questions = json.load(file)
    file.close()
    return questions


class Question:
    def __init__(self, text, level, correct_answer):
        self.score = 0
        self.question_of_user = None
        self.text = text
        self.level = level
        self.correct_answer = correct_answer
        self.answer = False

    def __repr__(self):
        return "Вопросик"

    def get_points(self):
        """Возвращает int, количество баллов.
         Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
         """

        if self.level == 1:
            self.score = 10
        elif self.level == 2:
            self.score = 20
        elif self.level == 3:
            self.score = 30
        elif self.level == 4:
            self.score = 40
        elif self.level == 5:
            self.score = 50
        else:
            self.score = "не знаю такую сложность, я сломалась"

        return self.score


    def is_correct(self):
         """Возвращает True, если ответ пользователя совпадает
           с верным ответов иначе False."""

         if self.correct_answer == self.answer:
             return True
         else:
             return False



    def build_question(self):
         """Возвращает вопрос в понятном пользователю виде, например:
             Вопрос: What do people often call American flag?
             Сложность 4/5
             """

         return f"Вопрос: {self.text} Сложность: {self.level}/5"

    def build_positive_feedback(self):
         """Возвращает :
            Ответ верный, получено __ баллов
            """

         return f"Ответ верный, получено {self.get_points()} баллов"

    def build_negative_feedback(self):
        """Возвращает :
        Ответ неверный, верный ответ __"""

        return f"Ответ неверный, верный ответ {self.correct_answer} "
