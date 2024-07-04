
# Глобальная таблица цифр римской системы записи чисел. Каждой цифре таблица
# сопоставляет её значение.
_roman_digit_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def decode_roman_number(roman_number : str) -> int:
    '''
    Преобразует строку, хранящую римскую запись некоторого числа, назад в это
    число. Параметр roman_number должен содержать корректно записанное римское
    число. Функция не считает ошибкой отклонение от строгих правил записи
    вычитания и спокойно декодирует исторические формы вроде IIX или DM. Пустая
    строка не считается правильным римским числом.
    '''

    def raise_error():
        raise ValueError(f'incorrect roman number: {roman_number}')

    if roman_number == '':
        raise_error()

    # Слегка приведём аргумент в порядок: сделаем буквы заглавными и удалим
    # возможные лишние пробелы.
    roman_number = roman_number.upper().strip()

    # Основная идея алгоритма: если всякая встретившая в числе цифра
    # засчитывается в плюс, если стоит в своём "правильном" порядке, и в минус,
    # если стоит в неправильном порядке. Порядок является неправильным, если
    # справа от числа стоит число, большее по значению, в противном случае,
    # порядок является правильным.
    #
    # Для того, чтобы не проверять для каждой цифры её соседа справа, будем
    # сканировать строку справа налево и учитывать порядок в переменной order.
    #
    # Нужно заметить, что по современным правилам записи при использовании
    # "правила вычитания" не допускаются повторения вычитаемой цифры, и сама
    # вычитаемая цифра может быть только I, X или C, и не использование
    # вычитания, где оно возможно, является ошибкой. Однако, в древности,
    # правила, вероятно, были менее строгими (так, IIII до сих пор встречаются
    # на часах). Примеры есть тут: https://en.wikipedia.org/wiki/Roman_numerals
    #
    # Поэтому реализованный тут алгоритм пермиссивный: он правильно декодирует
    # не только числа, записанные по строгим правилам, но и числа, записанные с
    # вариациями, главное, чтобы в них соблюдался общий принцип.

    result = 0
    order = 1
    for digit in reversed(roman_number):
        digit_value = _roman_digit_values.get(digit)
        if digit_value is None:
            raise_error()

        if digit_value < order:
            result -= digit_value
        else:
            result += digit_value
            order = digit_value

    if result <= 0:
        raise_error()

    return result


def test_number(number: int, roman_number: str):
    '''
    Проверяет, что римская запись roman_number действительно декодируется в
    число number. И для наглядности делает отладочную печать.
    '''
    assert number == decode_roman_number(roman_number)
    print(number , ':', roman_number)


def test_number_all():
    '''
    Проводит исчерпывающую проверку при помощи сторонней библиотеки roman.
    Проверяются все чисел от 1 до 4999 (это самое больше число, которое
    поддерживает эта библиотека). Для всех этих чисел проверяется, что результат
    декодирования совпадает с тем, что было закодировано.

    Чтобы использовать эту функцию установите библиотеку

        $ pip install roman

    и раскомментируйте строчку в функции test.
    '''
    import roman

    for number in range(1, 5000):
        roman_number = roman.toRoman(number)
        test_number(number, roman_number)


def test():
    '''
    Прогоняет все тесты для функции decode_roman_number.
    '''
    test_number(1, 'I')
    test_number(2, 'II')
    test_number(3, 'III')
    test_number(4, 'IIII')
    test_number(4, 'IV')
    test_number(5, 'V')
    test_number(6, 'VI')
    test_number(7, 'VII')
    test_number(8, 'VIII')
    test_number(9, 'VIIII')
    test_number(9, 'IX')

    # Полная проверка (требует внешнюю библиотеку).
    # test_number_all()


def manual_input():
    roman_number = input("Enter a roman number: ")

    number = decode_roman_number(roman_number)
    print(number)


if __name__ == '__main__':
    #test()
    manual_input()
