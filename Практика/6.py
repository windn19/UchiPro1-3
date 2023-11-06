


def trib():
    f1, f2, f3 = 0, 0, 1
    while True:
        yield f1
        f1, f2, f3 = f2, f3, f1 + f2 + f3


n = int(input())
seq = trib()
for i in range(n):
    print(next(seq), end=' ')
