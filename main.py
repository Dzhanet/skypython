# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from lesson_code.pin import check_pin
print("Введите ваш пин-код")
user_input = input()
if check_pin(user_input) == True:
    print("Такой пин-код подходит")
elif check_pin(user_input) == False:
    print("Такой пин-код НЕ подходит")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
