students = [('Oleg', [4, 4, 4]), ('Ivan', [3, 4, 5]), ('Lev', [3, 3, 3])]
students.sort(key=lambda value: (sum(value[1]), value[0]))
print(*[value[0] for value in students])