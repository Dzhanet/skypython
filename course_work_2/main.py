import json
import random
import requests
import utils
import classes


def main():
    """Запуск программы"""

    print("Ввведите имя игрока")

    user_name = input()
    list_of_user_words = []

    player = classes.Player(name=user_name, used_words=list_of_user_words)  #создаем экземпляр класса Player

    print(f"Привет, {player}")
    word_for_player = utils.load_random_word() #получаем рандомное слово для угадывания и список допустимых подслов

    print(f"Составьте {word_for_player.count_words()} слов из слова {word_for_player}")
    print(f"Слова должны быть не короче {word_for_player.count_words_for_word()} букв")
    print("Чтобы закончить игру, угадайте все слова или напишите stop")
    print("Поехали, ваше первое слово?")

    for item in range(word_for_player.count_words()):   #запускаем цикл угадывания слов по длине списка подслов

        word_from_user = input()

        if word_for_player.check_words(word_from_user) and word_from_user not in player.used_words:
            player.add_word_to_used_words(word_from_user)
            print("Верно, возьми с полки пирожок")

        elif word_for_player.check_words(word_from_user) and word_from_user in player.used_words:
            print("Жулик, не жульничай! Уже было!")

        else:
            print("Неверно, готовь себе сам, ленивая жепка")

        if word_from_user == "stop" or word_from_user == "стоп":
            print("игра завершена!")
            break

        last_digit = int(player.count_used_words() % 10) #остаток от деления для оконачания слова при выводе итогов

        if 11 <= player.count_used_words() <= 19: #делаем окончания для вывода итогов
            morphy = "слов"
        elif last_digit == 1:
            morphy = "слово"
        elif 2 <= player.count_used_words() <= 4:
            morphy = "слова"
        else:
            morphy = "слов"

    print("Игра закончилась, ты сделал это!")
    print(f"Ты угадал {player.count_used_words()} {morphy}!")

main()
