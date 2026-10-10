
# Python 8 тип данных
#
# Изменяемый
#
# Неизменяемый
# int - 1, 4, 2, 4, -3, -6, 3
# str - 'main', 'python', '3', ''
# float - 12.5, 3.0, 1.5, -2.1
# bool - True, False
#
# Арифметикалык операциялар: +, -, *, /, //, %, **
# round()

# print() - Маалымат чыгарат
# input() - Маалымат алат
# Переменный - Маалымат сактайт
# Коментарий(#) - Кодду иштейт

# number = int(input('Сан жаз: '))
# print(number**2)

# number1 = int(input('Сан жаз: '))
# number2 = int(input('Сан жаз: '))
#
# print(number1 // number2)
# print(number1 % number2)


# bool - True, False
# >, <, ==, !=, >=, <=

# print(4+2 >= 2*2+2)


# if, elif, else

# number = int(input('Сан жаз: '))
#
# if number > 0:
#     print('Он сан')
# elif number < 0:
#     print('Терс сан')
# else:
#     print('Сан 0го барабар')

#
# age = int(input('Жашынды жаз: '))
# if age >= 18:
#     print('Жашы жеткен')
# else:
#     print('Жашы жете элек')

# Жашынды жаз: 18
# Жашы жеткен

# Жашынды жаз: 17
# Жашы жете элек

#
# color = input('Тус жаз: ')
# if color == 'жашыл':
#     print('От')
# elif color == 'кызыл':
#     print('Токто')
# elif color == 'сары':
#     print('Даярдан')
# else:
#     print('Светофордо мындай тус жок')


country = input('Олконду жаз: ')
if country == 'Кыргызстан':
    print('Салам')
elif country == 'Россия':
    print('Привет')
else:
    print('Hello')

# Олконду жаз: Кыргызстан
# Салам

# Олконду жаз: Россия
# Привет

# Олконду жаз: Кытай
# Hello

# Олконду жаз: Америка
# Hello