lst = [1, 2, 3]
for elem in lst:
    print(lst)

lst = [1, 2, 3]
lst_iter = iter(lst)
while True:
    try:
        print(next(lst_iter))
    except StopIteration:
        break
