import random

N = int(input("Введите количество столбцов (N): "))
M = int(input("Введите количество строк (M): "))
matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(M)]
for row in matrix:
    print(row)
count = 0
c = []
for x in range(0, N):
    for i in range(0, M):
        c.append(matrix[i][count])
    count += 1
print(c)
print(c[2])