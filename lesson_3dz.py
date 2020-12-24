# Задание 1) вывести все числа небольше  100  которые делятся на 7
# lst = range(0, 100)
# for lst in lst:
#     if lst % 7 == 0:
#         print(lst)


# Задание 2) запросить имя и пол 5 человек, вывести в отдельном списке мужчин, в отдельном женщин
# sex = input("Введите ваш пол: ")
# name = input("Введите ваше имя: ")
# man = list()
# woman = list()
# while True:
#     if sex == "М":
#         man.append(name)
#     elif sex == "Ж":
#         woman.append(name)
#     print(man)

# Задание 3) написать программу, которая конвертирует введенный текст в текст лесенкой

# text = input("Введенный вами текст выведется лесенкой:  ")
# lst = text
# for lst in lst:
#
#     print(lst.upper())


# Задание 4) проверить относится элемент списка vse к фруктам или овощам используя цикл

# vse = ['kartoshka', 'smorodina', 'yabloki', 'grushi', 'morkovka', 'luk', 'pomidor', 'apelsini', 'arbuz']
# ovoshi = ['kartoshka', 'morkovka', 'luk', 'pomidor']
# frukti = ['yabloki', 'grushi', 'apelsini']
#
# for vse in vse:
#     if vse not in frukti and vse not in ovoshi:
#         print("Это ягоды: ", vse)
# for vse in ovoshi:
#     if vse in ovoshi:
#         print("Список овощей: ", vse)
# for vse in frukti:
#     if vse in frukti:
#         print("Это фруктовые: ", vse)
