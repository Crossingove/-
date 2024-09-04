import os
import datetime
import random
import time  # Импортируем модуль для управления временем

def generate_value(min_value, max_value):
    # Генерирует одно значение в заданном диапазоне
    return random.uniform(min_value, max_value)

def calculate_asymmetry_coefficients(H1, H2, r1, r2, Ik1, Ik2):
    # Расчет значений I1 и I2
    I1 = H1 * 2 * 3.14 * r1
    I2 = H2 * 2 * 3.14 * r2

    # Расчет коэффициента асимметрии сигнального тока
    Kask = abs((Ik1 - Ik2) / (Ik1 + Ik2)) * 100

    # Расчет коэффициента асимметрии тягового тока
    Katt = abs((I1 - I2) / (I1 + I2)) * 100

    # Расчет общего коэффициента асимметрии
    Kas = abs(Katt - Kask)

    return Kask, Katt, Kas

def write_results_to_file(file_path, Kask, Katt, Kas, r1, r2, Ik1, Ik2, H1, H2):
    # Формируем строку с результатами, включая H1 и H2
    result_line = (
        f"{datetime.datetime.now()} - Kask: {Kask:.2f}%, Katt: {Katt:.2f}%, Kas: {Kas:.2f}%, "
        f"r1: {r1:.3f}, r2: {r2:.3f}, Ik1: {Ik1:.2f}, Ik2: {Ik2:.2f}, "
        f"H1: {H1:.2f}, H2: {H2:.2f}\n"
    )
    # Открываем файл и записываем строку
    with open(file_path, 'a+') as file:
        file.write(result_line)

def main():
    # Задаем путь к файлу для записи результатов
    results_file_path = 'results.txt'

    # Задаем диапазоны значений
    H1_range = [300, 330]
    H2_range = [300, 330]
    r1_range = [0.15, 0.165]
    r2_range = [0.15, 0.165]
    Ik1_range = [10, 11]
    Ik2_range = [10, 11]

    for _ in range(100):  # Примерное количество итераций
        # Генерируем начальные значения
        H1 = generate_value(H1_range[0], H1_range[1])
        H2 = generate_value(H2_range[0], H2_range[1])
        r1 = generate_value(r1_range[0], r1_range[1])
        r2 = generate_value(r2_range[0], r2_range[1])
        Ik1 = generate_value(Ik1_range[0], Ik1_range[1])
        Ik2 = generate_value(Ik2_range[0], Ik2_range[1])

        # Расчет коэффициентов
        Kask, Katt, Kas = calculate_asymmetry_coefficients(H1, H2, r1, r2, Ik1, Ik2)

        # Записываем результаты в файл, включая значения H1 и H2
        write_results_to_file(results_file_path, Kask, Katt, Kas, r1, r2, Ik1, Ik2, H1, H2)

        # Выводим результаты на экран, включая H1 и H2
        print(f"Напряженность первой катушки = {H1:.2f} A/m")
        print(f"Напряженность второй катушки = {H2:.2f} A/m")
        print(f"Сигнальный ток первой катушки = {Ik1:.2f} A")
        print(f"Сигнальный ток второй катушки = {Ik2:.2f} A")
        print(f"Высота первой катушки = {r1:.3f} м")
        print(f"Высота второй катушки = {r2:.3f} м")
        print(f"Коэффициент асимметрии сигнального тока = {Kask:.2f} %")
        print(f"Коэффициент асимметрии тягового тока = {Katt:.2f} %")
        print(f"Общий коэффициент асимметрии = {Kas:.2f} %")

        # Проверяем на критический уровень асимметрии
        if Kas > 4:
            print("Критический уровень асимметрии!!!")
            print(datetime.datetime.now())

        # Задержка перед следующей итерацией
        time.sleep(2)

if __name__ == "__main__":
    main()
