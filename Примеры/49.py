def generator():
    i = 1
    yield i
    i += 1
    yield i
    i += 1
    yield i


g = generator()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # ошибка StopIteration
