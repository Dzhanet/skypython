class BasicWord:

    def __init__(self, word, list_words):

        self.word = word
        self.list_words = list(list_words)

    def __repr__(self):

        return self.word

    def check_words(self, word_from_user):
        """Проверяем, есть ли слово от пользователя в списке подслов"""

        if word_from_user in self.list_words:
            return True
        else:
            return False

    def count_words(self):
        """Считаем количество подслов в списке self.list_words и возвращаем в int"""

        return int(len(self.list_words))

    def count_words_for_word(self):
        """Находим минимальное значение среди подслов в self.list_words и возвращаем длину"""

        return len(min((word for word in self.list_words if word), key=len))




class Player:

    def __init__(self, name, used_words):

        self.name = name
        self.used_words = list(used_words)

    def __repr__(self):

        return self.name


    def count_used_words(self):
        """Считаем количество слов"""

        return int(len(self.used_words))

    def add_word_to_used_words(self, word_from_user):
        """добавляем слово от пользователя в список использованных слов"""

        self.used_words.append(word_from_user)

    def check_used_word(self, word_from_user):
        """проверяем, есть ли введенное пользователем слово в списке подслов"""

        if word_from_user in self.used_words:
            return True
        else:
            return False
