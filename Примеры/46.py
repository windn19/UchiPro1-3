lst = [1, 2, 3]
lst_iter = iter(lst)

print(next(lst_iter))  # 1
print(next(lst_iter))  # 2
print(next(lst_iter))  # 3
print(next(lst_iter))  # ошибка StopIteration
