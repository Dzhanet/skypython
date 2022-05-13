import json
import random
import functions_for_hw_8


def main():
    """запуск программы"""

    questions_list = []
    list_of_instances = []
    counter_right_questions = 0
    counter_score = 0

    questions_list = functions_for_hw_8.load_questions()
    for line in questions_list:
        Question_1 = functions_for_hw_8.Question(text=line["q"], level=int(line["d"]), correct_answer=line["a"]) #указываем параметры, чтобы не путаться
        list_of_instances.append(Question_1)

    print("Игра начинается!")

    random.shuffle(list_of_instances)

    for item in list_of_instances:
        print(item.build_question())
        user_input = input()
        item.answer = user_input

        if item.is_correct():
            counter_score += item.get_points()
            counter_right_questions += 1
            print(item.build_positive_feedback())
        else:
            print(item.build_negative_feedback())

    def statistics():
        """Собираем статистику по очкам и правильным ответам"""

        print("Вот и всё!")
        print(f"Отвечено на {counter_right_questions} из {len(list_of_instances)} вопросов")
        print(f"Набрано баллов: {counter_score}")

    statistics()
main()