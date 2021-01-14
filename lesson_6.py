from mymath import other
import mymath as m
import mymath.operations.trigonometric as trig


m.operations.arithmetic.add()


option = input("Какую команду выполнить?" "\n"
               "1)Найти синус" " "
               "2)Найти косинус: " " "
               "3)Округлить число: ")
if option == '1':
    # Sinus
    sin = int(input("Введите значене для стороны a треугольника: "))
    sin2 = int(input("Введите значене для стороны b треугольника: "))
    print("Синус abc = ", trig.sine(sin, sin2))

elif option == '2':
    # Cosine
    cos = int(input("Введите значене для стороны b треугольника: "))
    cos2 = int(input("Введите значене для стороны c треугольника: "))
    print("Синус abc = ", trig.sine(cos, cos2))

elif option == '3':
    # Round
    rounding = float(input("Введите десятичное число чтобы округлить: "))
    print(other.rounds(rounding))

