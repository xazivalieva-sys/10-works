import random

N = int(input("Введите количество столбцов (N): "))
matrix = [[random.randint(1, 100) for _ in range(N)] for _ in range(N)]
for row in matrix:
    print(row)

count = 0

for i in range(0, N):
    a = matrix[i][i]
    print(a, end=' ')
    if a % 3 == 0:
        count += 1
print()
print(f'Количество значений на главной диагонали, деленных на 3 без остатка: {count}')
