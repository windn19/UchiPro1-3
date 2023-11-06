def average(a, b, c, precision=0):
    result = (a + b + c) / 3
    return round(result, precision)


lst = [1, 2, 3]
print(average(*lst))
