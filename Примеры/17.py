def average(a, b, c, precision=0):
    result = (a + b + c) / 3
    return round(result, precision)


print(average(2, 3, 3, precision=3))  # 2.667
print(average(2, 3, 3, 1))  # 2.7
print(average(2, 3, 3))  # 3.0
