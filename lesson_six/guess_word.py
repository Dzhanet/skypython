import random

def update_user_data(name_input,counter_score):
    """Записываем в "history.txt имя пользователя + колво очков"""

    with open("history.txt", "a") as file:
        file.write(f"{name_input} {counter_score}\n")

def do_list_from_words():
    """Делаем список из words для random_words"""

    with open("words.txt", "rt") as file:
        list_words = [line.strip() for line in file]
    return list_words

def collect_statistics():
    """собираем статистику"""


    scores = []
    game_count = 0
    with open("history.txt", "rt") as file:
        for line in file:
            game_count += 1
            score = line.strip().split(" ")
            scores.append(score[1])

        max_score = max(scores)
        print (f"Всего игр сыграно: - {game_count}. Максимальный рекорд: {max_score}")


def main():
    """основная функция по угадыванию слов"""


    counter_score = 0
    words = do_list_from_words()

    for word in words:
        new_word = ''.join(random.sample(word, len(word)))
        print(f"Угадайте слово: {new_word}")
        user_answer = input()
        if user_answer == word:

          counter_score += 10
          print(f"Верно! Вы получаете {counter_score} очков.")
        else:
          print(f"Неверно! Верный ответ – {word}")

    update_user_data(name_input, counter_score)
    collect_statistics()

name_input = input("Введите ваше имя: ")

main()
