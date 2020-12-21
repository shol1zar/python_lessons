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
