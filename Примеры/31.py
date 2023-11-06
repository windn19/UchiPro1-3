res_1 = filter(str.isalpha, ['hello', '123', 'python'])
res_2 = filter(lambda x: x % 2 == 0, range(1, 5))
res_3 = filter(lambda x: x < 0, [10, 4, 2, -1, 6])
res_4 = filter(lambda x: x > 10, map(lambda x, y: x + y, range(1, 5), range(5, 10)))
print(res_1)  # <filter object at 0x0000019FBD94BE80>
print(list(res_1))  # ['hello', 'python']
print(list(res_2))  # [2, 4]
print(list(res_3))  # [-1]
print(list(res_4))  # [12]
