from functools import reduce

res_1 = reduce(lambda x, y: x + y, range(1, 5))  # ((((1 + 2) + 3) + 4) + 5)
res_2 = reduce(lambda x, y: x + y, range(1, 5), 10)
res_3 = reduce(lambda x, y: y + x, 'hello')
res_4 = reduce(lambda x, y: [y] + x, [1, 2, 3, 4, 5], [])
print(res_1)  # 10
print(res_2)  # 20
print(res_3)  # olleh
print(res_4)  # [5, 4, 3, 2, 1]
