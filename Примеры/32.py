from functools import reduce

result = reduce(lambda x, y: x + y, map(int, input().split()))
