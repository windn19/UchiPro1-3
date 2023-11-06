res_1 = all([1, 2, 3, 0, 1])
res_2 = all(map(str.isalpha, ['hello', '123', 'python']))
res_3 = all(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
res_4 = any(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
print(res_1)  # False
print(res_2)  # False
print(res_3)  # False
print(res_4)  # True
