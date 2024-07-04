
def is_monotonic(arr) -> bool:
    '''
    Проверяет, что список arr - монотонный, то есть его элементы или все идут в
    неубывающем порядке, или все идут в невозрастающем порядке.
    
    Некоторые частные случаи:
    * пустой массив - монотонный;
    * массив из одного элемента - монотонный;
    * массив из любых двух элементов - монотонный.
    '''

    if len(arr) <= 2:
        return True

    expected_direction = None

    prev = arr[0]
    for cur in arr:
        if expected_direction is None:
            if prev < cur:
                # Возрастающая последовательность.
                expected_direction = 1
            elif prev > cur:
                # У последовательность.
                expected_direction = -1
        else:
            if prev < cur and expected_direction == -1:
                return False

            if prev > cur and expected_direction == 1:
                return False

        prev = cur

    return True


def test_is_monotonic(expected_result: bool, arr):
    '''
    Проверяет, что функция is_monotonic от списка arr возвращает значение
    expected_result. Для наглядности делает отладочную печать.
    '''

    assert expected_result == is_monotonic(arr)
    print (arr, ":", expected_result)

    # Если список монотонный, то его перестановка в обратном порядке также
    # монотонная. Проверим заодно и её.
    assert expected_result == is_monotonic(list(reversed(arr)))


def test():
    '''
    Прогоняет тесты для функции is_monotonic.
    '''
    test_is_monotonic(True, [])
    test_is_monotonic(True, [1])
    test_is_monotonic(True, [1, 1])
    test_is_monotonic(True, [1, 1, 1, 1, 1, 2])
    test_is_monotonic(True, [1, 1, 1, 1, 1, -2])

    test_is_monotonic(False, [1, 3, 2])
    test_is_monotonic(False, [1, 1, 1, 1, 1, 2, 1])


def manual_input():
    '''
    Выполняет ручной ввод списка чисел и выполняет от него функцию is_monotonic.
    Для ручной отладки.
    '''
    seq_text = input('Enter a space-separated sequence of numbers: ')
    arr = [float(s) for s in seq_text.split()]
    print(is_monotonic(arr))


if __name__ == '__main__':
    #test()
    manual_input()
