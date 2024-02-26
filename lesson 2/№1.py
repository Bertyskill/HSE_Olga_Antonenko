"""1. Создайте ряд функций для проведения математических вычислений:
● функция вычисления факториала числа (произведение натуральных чисел от 1
до n). Принимает в качестве аргумента число, возвращает его факториал;
● поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из
трёх чисел, возвращает наибольшее из них;
● расчёт площади прямоугольного треугольника. Принимает в качестве аргумента
размер двух катетов треугольника. Возвращает площадь треугольника."""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Введите число: "))
if number < 0:
    print("Факториал числа не определен")
elif number == 0:
    print("Факториал 0 равен 1")
else:
    print("Факториал числа", number, "равен", factorial(number))


def find_max_of_three_numbers():
    numbers = [int(input("Введите первое число: ")),
               int(input("Введите второе число: ")),
               int(input("Введите третье число: "))]

    max_number = max(numbers)

    print("Наибольшее число:", max_number)


find_max_of_three_numbers()


def calculate_area_of_right_triangle(cathetus1, cathetus2):
    area = 0.5 * cathetus1 * cathetus2
    return area

cathetus1 = float(input("Введите длину катета: "))
cathetus2 = float(input("Введите длину катета: "))

if cathetus1 <= 0 or cathetus2 <= 0:
    print("Введите положительные числа.")

else:
    triangle_area = calculate_area_of_right_triangle(cathetus1, cathetus2)
    print("Площадь прямоугольного треугольника", cathetus1, "и", cathetus2, "равна", triangle_area)

    """2. Создайте функцию для генерации текста с адресом суда.
Функция должна по шаблону генерировать шапку для процессуальных документов с
реквизитами сторон для отправки.
Пример работы функции:
В арбитражный суд города Москвы
Адрес: 115225, г. Москва, ул. Б. Тульская, 17
Истец: Пупкин Василий Геннадьевич
ИНН 1236182357 ОГРНИП 218431927812733
Адрес: 123534, г. Москва, ул. Водников, 13
Ответчик: ООО “Кооператив Озеро”
ИНН 1231231231 ОГРН 123124129312941
Адрес: 123534, г. Москва, ул. Красивых молдавских партизан, 69
Номер дела А40-123456/2023"""
