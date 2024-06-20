import datetime

while True:
    try:
        H1 = float(input("Введите значение H1: "))
        H2 = float(input("Введите значение H2: "))
        r1 = float(input("Введите значение r1: "))
        r2 = float(input("Введите значение r2: "))
        Ik1 = float(input("Введите значение Iк1: "))
        Ik2 = float(input("Введите значение Iк2: "))
    except ValueError:
        print("Внимание! Отсутствуют входные данные")
        break

    I1 = H1 * 2 * 3.14 * r1
    I2 = H2 * 2 * 3.14 * r2
    Katt = abs((I1 - I2) / (I1 + I2)) * 100
    Kask = abs(Ik1 - Ik2) / (Ik1 + Ik2) * 100
    Kas = abs(Katt - Kask)

    print(f"Высота первой катушки = {r1}м")
    print(f"Высота второй катушки = {r2}м")
    print(f"Коэффициент асимметрии сигнального тока = {Kask:.2f}%")
    print(f"Коэффициент асимметрии тягового тока = {Katt:.2f}%")
    print(f"Общий коэффициент асимметрии = {Kas:.2f}%")

    if Kas > 4:
        print("Критический уровень асимметрии!!!")
        print(datetime.datetime.now())