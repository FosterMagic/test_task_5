from typing import List, Tuple
from math import sqrt

"""
Выполните тестовое задание, чтобы мы понимали уровень вашей подготовки.
Задание в Python:
1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.
2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
3. Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы для
 инициализации координат точки, вычисления расстояния до другой точки, а также для получения и изменения координат.
4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
P.S. Результатом отправьте ссылку на GitHub репозиторий.
"""


# подзадача 1
def unique(nums: list) -> list:
    unique_nums = list(set(nums))
    return unique_nums


# подзадача 2
# считаем количество простых чисел в диапазоне от 2 до n

def count_prime_numbers(num):
    prime_numbers = []
    for i in range(2, num + 1):
        for j in prime_numbers:
            if j > int((sqrt(i)) + 1):
                prime_numbers.append(i)
                break
            if (i % j == 0):
                break
        else:
            prime_numbers.append(i)
    return prime_numbers


# считаем количество простых чисел в произвольном диапазоне

def count_prime_number_in_range(num1, num2):
    lst1 = count_prime_numbers(num1)
    lst2 = count_prime_numbers(num2)
    return [elem for elem in lst2 if elem not in lst1]


print(count_prime_number_in_range(10, 100))


# подзадача 3
# работа с классом "Точка"

class Point:

    def __init__(self, x1=1, y1=1):
        self.move(x1, y1)

    def move(self, x2, y2):
        self.x1 = x2
        self.y1 = y2

    def get(self):
        print(f"Point with x-coord:  {self.x1} and y-coord: {self.y1}")

    def distance(self, diff_point):
        if not isinstance(diff_point, Point):
            raise ValueError('Argument must belong to Point class')
        return sqrt((abs(self.x1 - diff_point.x1)) ** 2 + (abs(self.y1 - diff_point.y1) ** 2))


# подзадача 4
def sort_len(text: List[str]) -> List[str]:
    lst1 = sorted(text, key=len)
    lst2 = sorted(lst1, key=len, reverse=True)
    return lst2


print(sort_len(['Ivan', 'Peter', 'Michael']))
