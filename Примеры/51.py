g = (i for i in range(5))
print(g)  # <generator object <genexpr> at 0x000002069FD49FC0>
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 4
print(next(g))  # ошибка StopIteration
