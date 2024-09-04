import os
import datetime
import math
import logging

def read_values_from_files(file_paths):
    values = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            value = float(file.readline().strip())
            values.append(value)
    return values


# Функция для расчета коэффициентов асимметрии
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

def write_results_to_file(Kask, Katt, Kas, r1, r2, Ik1, Ik2):
    log_file_path = os.path.join('log.txt')
    logging.basicConfig(filename=log_file_path, level=logging.DEBUG)
    logging.debug(f"Kask: {Kask}, Katt: {Katt}, Kas: {Kas}")
    logging.debug(f"r1: {r1}, r2: {r2}")
    logging.debug(f"Ik1: {Ik1}, Ik2: {Ik2}")
    logging.debug(datetime.datetime.now())


# Предположим, что есть следующие файлы:
#   - h1.txt содержит значение Н1
#   - h2.txt содержит значение Н2
#   - r1.txt содержит значение r1
#   - r2.txt содержит значение r2
#   - ik1.txt содержит значение Iк1
#   - ik2.txt содержит значение Iк2
def main():
    # Предполагаемые пути к файлам (без указания директории)
    h1_file_path = 'h1.txt'
    h2_file_path = 'h2.txt'
    r1_file_path = 'r1.txt'
    r2_file_path = 'r2.txt'
    ik1_file_path = 'ik1.txt'
    ik2_file_path = 'ik2.txt'

    # Читаем значения из файлов
    H1, H2, r1, r2, Ik1, Ik2 = read_values_from_files(
        [h1_file_path, h2_file_path, r1_file_path, r2_file_path, ik1_file_path, ik2_file_path])

    # Вызываем функцию для расчета коэффициентов асимметрии
    Kask, Katt, Kas = calculate_asymmetry_coefficients(H1, H2, r1, r2, Ik1, Ik2)

    # Запись результатов в файл
    write_results_to_file(Kask, Katt, Kas, r1, r2, Ik1, Ik2)

    # Выводим результаты
    print(f"Высота первой катушки = {r1}м")
    print(f"Высота второй катушки = {r2}м")
    print(f"Коэффициент асимметрии сигнального тока = {Kask} %")
    print(f"Коэффициент асимметрии тягового тока = {Katt} %")
    print(f"Общий коэффициент асимметрии = {Kas} %")

    # Проверяем на критический уровень асимметрии
    if Kas > 4:
        print("Критический уровень асимметрии!!!")
        print(datetime.datetime.now())

if __name__ == "__main__":
    main()
#В каждом текстовом файле только одно значение