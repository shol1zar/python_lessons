import os
# написать программу, которая запрашивает и сохраняет данные о пользователе в файл
# для каждого пользователя заводится отдельный файл, предварительно проверив, есть ли уже с таким именем
# у программы три режима работы - вывод всех файлов с пользователями; выбор файла и вывод данных;
# создание новой записи, путем введения новых данных;

if not os.path.isdir("lesson_5_2/"):
    os.mkdir("lesson_5_2/")


name = input("Введите ваше имя : ")
surname = input("Введите вашу фамилию: ")
file = "lesson_5_2/" + name + ".txt"
s = name + " " + surname + " "


check = os.listdir("lesson_5_2/")
for i in check:
    if i in file:
        print(i, "уже существует и будет перезаписан")

f = open(file, 'w')
f.write(s)
f.close()

while True:
    option = input("Что делать с файлом?  "
                   "1)Показать все в папке  "
                   "2)Выбрать файл  "
                   "3)Добавить в файл  "
                   "4)Создать новый файл  "
                   "5)Завершить: ")
    if option == "1":
        directory = os.listdir('lesson_5_2/')
        for index, file in enumerate(directory):
            print(index, ':', file)

    elif option == "2":
        select = input("Выберите файл: ")
        path = "lesson_5_2/" + select + ".txt"
        with open(path, "r") as f:
            print('readline: ', f.readlines())

    elif option == "3":
        add = input("Выберите файл чтобы добавить инфу: ")
        add2 = "lesson_5_2/" + add + ".txt"
        with open(add2, 'a') as f:
            add3 = input("Введите доп инфу: ")
            f.write(" " + add3)

        with open(add2, 'r') as file_content:
            print('readline: ', file_content.readlines())

    elif option == "4":
        name = input("Введите ваше имя : ")
        surname = input("Введите вашу фамилию: ")
        file = "lesson_5_2/" + name + ".txt"
        s2 = name + " " + surname + " "

        check = os.listdir("lesson_5_2/")
        for i in check:
            if i in file:
                print(i, "уже существует и будет перезаписан")

        f = open(file, "w")
        f.write(s2)
        f.close()

    elif option == "5":
        break
