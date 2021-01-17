from mymath import other
import mymath as m
import mymath.operations.arithmetic as arith
import mymath.operations.trigonometric as trig


while True:

    option = input("Какую команду выполнить?" "\n"
                   "1)Найти синус" " "
                   "2)Найти косинус" " "
                   "3)Округлить" " "
                   "4)Сумма" " "
                   "5)Разность" " "
                   "6)Минимум" " "
                   "7)Максиум" " "
                   "8)Завершить: ")

    if option == '1':
        # Sine
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

    elif option == '4':
        # Add
        int1 = int(input("Число 1: "))
        int2 = int(input("Число 2: "))
        print("Сумма = ", m.operations.arithmetic.add(int1, int2))

    elif option == '5':
        # Subtract
        int1 = int(input("Число 1: "))
        int2 = int(input("Число 2: "))
        print("Разность = ", m.operations.arithmetic.subtract(int1, int2))

    elif option == '6':
        # Min
        print(other.minimum())

    elif option == '7':
        # Max
        print(other.maximum())

    elif option == '8':
        break
