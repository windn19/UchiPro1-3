res_1 = enumerate('hello')
res_2 = enumerate(['a', 'b', 'c'], start=5)

print(res_1)  # <enumerate object at 0x0000026C167E4940>
print(list(res_1))  # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
print(list(res_2))  # [(5, 'a'), (6, 'b'), (7, 'c')]
