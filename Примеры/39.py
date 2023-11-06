res_1 = zip([1, 2, 3], 'abc')
res_2 = zip(range(10), 'abc')
res_3 = zip(range(5), 'hello', [1, 2, 3, 4, 5, 6, 7])
print(res_1)  # <zip object at 0x000001D7F321E300>
print(list(res_1))  # [(1, 'a'), (2, 'b'), (3, 'c')]
print(dict(res_2))  # {1: 'a', 2: 'b', 3: 'c'}
print(list(res_3))  # [(0, 'h', 1), (1, 'e', 2), (2, 'l', 3), (3, 'l', 4), (4, 'o', 5)]