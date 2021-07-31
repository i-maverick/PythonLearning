from bisect import bisect
from typing import Callable, List, Tuple


def binary_search(arr: List[int], val: int) -> int:
    """
    Бинарный поиск элемента в упорядоченном массиве. O(log(n))
    Нужен для определения стартовой позиции, чтоб не итерироваться по всему массиву
    """
    idx = bisect(arr, val)
    if idx == 0:
        return -1
    elif arr[idx - 1] == val:
        return idx - 1
    else:
        return -1


def is_not_empty(left: list, right: list) -> bool:
    """
    Проверка, что оба массива не пустые
    """
    if not all([left, right]):
        print(f"Array or subarray cannot be empty: {left}, {right}")
        return False
    return True


def array_is_longer(left: list, right: list) -> bool:
    """
    Проверка, что подмассив не длиннее массива
    """
    if len(left) < len(right):
        print(f"Subarray cannot be longer than array: {left}, {right}")
        return False
    return True


def validate(checks: Tuple[Callable]):
    """
    Декоратор для валидации входных данных
    """
    def outer(func):
        def inner(*args, **kwargs):
            if all([check(*args, **kwargs) for check in checks]):
                return func(*args, **kwargs)
        return inner
    return outer


def compare(arr: List[int], sub: List[int]) -> bool:
    """
    Проверка вхождения подмассива в массив, при условии совпадения первого элемента
    """

    for x, y in zip(arr, sub):
        if x != y:
            if x == arr[0]:
                # Первый элемент может повторяться (пример - ряд Фибоначчи), поэтому пробуем сдвинуть массив на 1
                return compare(arr[1:], sub)
            return False
    return True


@validate(checks=(is_not_empty, array_is_longer))
def is_include(array: List[int], subarray: List[int]) -> bool:
    """
    Проверка вхождения подмассива в массив. O(k), где k - длина подмассива.
    """

    # Если первые элементы массивов совпадают, то итерируемся с начала
    if subarray[0] == array[0]:
        return compare(array, subarray)

    # Находим первый элемент подмассива в массиве через бинарный поиск
    start = binary_search(array, subarray[0])
    if start == -1:
        return False
    return compare(array[start:], subarray)


assert is_include([], []) is None
assert is_include([1], []) is None
assert is_include([1], [1, 2]) is None

fib_list = [1, 1, 2, 3, 5, 8, 13]
assert is_include(fib_list, [0]) is False
assert is_include(fib_list, [1]) is True
assert is_include(fib_list, [1, 1]) is True
assert is_include(fib_list, [1, 2]) is True
assert is_include(fib_list, [1, 3]) is False
assert is_include(fib_list, [2, 1]) is False
assert is_include(fib_list, [3, 5]) is True
assert is_include(fib_list, [1, 2, 3, 5]) is True
