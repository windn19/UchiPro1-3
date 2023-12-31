# 5. Напиши функцию-генератор number_generator() с параметрами start и stop, которая будет возвращать
# бесконечную зацикленную последовательность чисел от start до stop включительно.
# Считай с клавиатуры три целых числа – параметры start, stop (start <= stop) и количество чисел, которые нужно
# получить с помощью генератора number_generator(), и выведи эти числа.
#
# Пример работы программы:
# g = number_generator(7, 9)
# for i in range(6):
#    print(next(g))
# Вывод:
# 7
# 8
# 9
# 7
# 8
# 9
#
# Входные данные:
# Вводится три строки целых чисел: на первой строке параметр start, на второй строке параметр stop (start <= stop).
# На третьей строке вводится число n - количество чисел последовательности, которые нужно получить.
# Выходные данные:
# Выводится n целых чисел - каждое на отдельной строке.
#
# Пример ввода:
# 1
# 3
# 5
# Пример вывода:
# 1
# 2
# 3
# 1
# 2

def number_generator(start, stop):
    while True:
        for i in range(start, stop + 1):
            yield i


start = int(input())
stop = int(input())
n = int(input())
g = number_generator(start, stop)
for i in range(n):
    print(next(g))

# ввод начало, конец, количество в виде целых чисел
# создать генератора цифр с аргументами: начало, конец
# для каждого элемента от нуля до количества делай
#     печать следующего значения генератора цифр
#
# функция генератор цифр с параметрами начало, стоп
#     пока Истина делай
#         для каждого элемента последовательности от начала до стоп плюс 1 делай
#             запомни состояние и верни значение элемента
