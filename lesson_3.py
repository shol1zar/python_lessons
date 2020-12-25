month = int(input("Введите цифру месяца чтобы узнать время года:  "))


winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

if month in winter:
    print("Сейчас зима")
if month in spring:
    print("Сейчас весна")
if month in summer:
    print("Сейчас лето")
if month in autumn:
    print("Сейчас осень")
if month > 12:
    print("Есть только 12 месяцев")

# измените значения переменных ниже, чтобы все условия выполнились и
# распечатались числа от 1 до 6

# number = 16
# second_number = not 10
# first_array = [1, 2, 3]
# second_array = [1, 5]
#
#
# if number > 15:
#     print("1")
#
# if first_array:
#     print("2")
#
# if len(second_array) == 2:
#     print("3")
#
# if len(first_array) + len(second_array) == 5:
#     print("4")
#
# if first_array and first_array[0] == 1:
#     print("5")
#
# if not second_number:
#     print("6")
