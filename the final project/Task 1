def fib(n: int):
    """
    Возвращает генератор, возвращающий n первых членов последовательности
    Фибоначчи. Последовательность Фибоначчи понимается в форме с ведущим нулём:
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    Это важно, так как иногда в математике в её определении нуль опускается из
    тех или иных соображений.

    Параметр n должен быть неотрицательным. В случае n == 0 возвращается
    пустой генератор.
    """
    prev2 = 0
    prev1 = 1

    for _ in range(n):
        yield prev2
        summa = prev2 + prev1
        prev2 = prev1
        prev1 = summa


def test_fib(n: int, expected_result: list):
    '''
    Проверяет, что fib(n) даёт ожидаемый результат expected_result.
    '''
    assert list(fib(n)) == expected_result
    print(n, ':', expected_result)


def test():
    '''
    Выполняет тесты для функции fib.
    '''
    test_fib(0, [])
    test_fib(1, [0])
    test_fib(2, [0, 1])
    test_fib(3, [0, 1, 1])
    test_fib(4, [0, 1, 1, 2])
    test_fib(5, [0, 1, 1, 2, 3])
    test_fib(6, [0, 1, 1, 2, 3, 5])


def manual_input():
    '''
    Выполняет ввод числа n и выводит результат применения к нему функции fib.
    Для ручной отладки.
    '''
    n_text = input('Enter n: ')
    n = int(n_text)
    print(list(fib(n)))


if __name__ == '__main__':
    # test()
    manual_input()
