# Задание 1) вывести все числа небольше  100  которые делятся на 7
# lst = range(0, 100)
# for lst in lst:
#     if lst % 7 == 0:
#         print(lst)


# Задание 2) запросить имя и пол 5 человек, вывести в отдельном списке мужчин, в отдельном женщин

# i = 0
# man = list()
# woman = list()
#
# while i < 5:
#     sex = input("Введите ваш пол: ")
#     name = input("Введите ваше имя: ")
#     if sex == "М":
#         man.append(name)
#     elif sex == "Ж":
#         woman.append(name)
#         i += 1
#
# print("Список мужчин: ",  man)
# print("Список женщин: ", woman)


# Задание 3) написать программу, которая конвертирует введенный текст в текст лесенкой

# text = input("Введенный вами текст выведется лесенкой:  ")
# lesenka = " "
# for i in text:
#     if text.index(i) % 2 == 0:
#         lesenka = lesenka + i.upper()
#     else:
#         lesenka = lesenka + i.lower()
# print(lesenka)


# Задание 4) проверить относится элемент списка  к фруктам или овощам используя цикл while


vege = ['kartoshka', 'morkovka', 'luk', 'pomidor']
fruits = ['yabloki', 'grushi', 'apelsini']
berry = ['arbuz', 'smorodina', 'malina']
while True:
    check = input("Введите название продукта: ")
    if check in vege:
        print(check, "это овощь")
    elif check in fruits:
        print(check, " это фрукты")
    elif check in berry:
        print(check, "это ягода")
    else:
        print("Данного продукта нет в списке")
        break
