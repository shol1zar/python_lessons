import os
# написать программу, которая запрашивает и сохраняет данные о пользователе в файл
# для каждого пользователя заводится отдельный файл, предварительно проверив, есть ли уже с таким именем
# у программы три режима работы - вывод всех файлов с пользователями; выбор файла и вывод данных;
# создание новой записи, путем введения новых данных;


name = input("Введите ваше имя : ")
surname = input("Введите вашу фамилию: ")
file = "C:/Test_1/lesson_5_2/" + name + ".txt"
s = name + " " + surname + " "


check = os.listdir("lesson_5_2")
for i in check:
    if i in file:
        print(i, "уже существует вы хотите перезаписать?")
        answer = input("Да / Нет:  ")
        if answer == "Да".lower():
            f = open(file, 'w')
            f.write(s)
            f.close()
        elif answer == "Нет".lower():
            f = open(file)
            f.close()


f = open(file, 'w')
f.write(s)
f.close()


directory = os.listdir('lesson_5_2')
for index, file in enumerate(directory):
    print(index, ':', file)


select = input("Выберите файл: ")
path = "C:/Test_1/lesson_5_2/" + select + ".txt"
with open(path, "r") as f:
    print(f.readlines())


add = input("Выберите файл чтобы добавить инфу: ")
add2 = "C:/Test_1/lesson_5_2/" + add + ".txt"
with open(add2, 'a') as f:
    add3 = input("Введите доп инфу: ")
    f.write(" " + add3)

with open(add2, 'r') as file_content:
    print('readline: ', file_content.readlines())
