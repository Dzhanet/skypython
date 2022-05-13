from validators.validate_pin import validate_pin
from validators.validate_name import validate_card

print("Введите ваш номер карты")
card_number = input()

if validate_card(card_number) == True:
    print ("Номер карты допустимый")
elif validate_card(card_number) == False:
    print ("Номер карты недопустимый")

print("Введите ваш пин-код")
card_pin = input()

if validate_pin(card_pin) == True:
    print ("Пин код допустимый")
elif validate_pin (card_pin) == False:
    print ("Пин код недопустимый")