import logging

# Создаем новый логгер
logger = logging.getLogger("basiq")

# Cоздаем ему обработчик
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs/basiq.txt')

# Добавляем обработчик к журналу
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(asctime)s : %(message)s")
# Применяем форматирование к обработчику
console_handler.setFormatter(formatter_one)
file_handler.setFormatter(formatter_one)

# Добавлякем обработчик к журналу
logger.addHandler(console_handler)
logger.addHandler(file_handler)
