def func(x):
    return x ** 2


res_1 = map(len, ['hello', '123', 'python'])
res_2 = map(str.upper, ['hello', '123', 'python'])
res_3 = map(func, range(1, 5))
res_4 = map(lambda x: x ** 2, range(1, 5))
res_5 = map(lambda x, y: x + y, range(1, 5), range(5, 10))

print(res_1)  # <map object at 0x000001798FAABE80>
print(list(res_1))  # [5, 3, 6]
print(list(res_2))  # ['HELLO', '123', 'PYTHON']
print(list(res_3))  # [1, 4, 9, 16]
print(list(res_4))  # [1, 4, 9, 16]
print(list(res_5))  # [6, 8, 10, 12]
