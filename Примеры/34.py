lst = [(5, 6), (121, 11), (20, 1, 1), (1, 2, 1)]
result = filter(lambda s: s == s[::-1],
                map(lambda x: str(sum(x)),
                    lst))
print(*result)