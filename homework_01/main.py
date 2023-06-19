"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in nums]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime" 


def is_prime(number: int) -> bool:
    if number > 1:
        for num in range(2, round(number ** 0.5) + 1):
            if number % num == 0:
                return False
        return True


def is_odd(number: int) -> bool:
    return number % 2 != 0


def is_even(number: int) -> bool:
    return number % 2 == 0


def filter_numbers(numbers: list, numbers_type: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    numbers_type = numbers_type.lower()

    if numbers_type not in [EVEN, ODD, PRIME]:
        print('Incorrect additional argument')
        return []
    if numbers_type == EVEN:
        return list(filter(is_even, numbers))
    if numbers_type == ODD:
        return list(filter(is_odd, numbers))
    if numbers_type == PRIME:
        return list(filter(is_prime, numbers))
