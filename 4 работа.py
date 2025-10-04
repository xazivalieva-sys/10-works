M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
matrix = []
print("Введите элементы матрицы построчно:")
for i in range(M):
    row = list(map(float, input(f"Строка {i + 1}: ").split()))
    matrix.append(row)
min_in_rows = []
for i in range(M):
    min_val = matrix[i][0]
    min_col = 0
    for j in range(1, N):
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_col = j
    min_in_rows.append((min_val, i, min_col))
max_of_mins = min_in_rows[0]
for item in min_in_rows[1:]:
    if item[0] > max_of_mins[0]:
        max_of_mins = item
print("\nМинимальные элементы в каждой строке:")
for val, row, col in min_in_rows:
    print(f"Строка {row + 1}: минимальный элемент = {val} (столбец {col + 1})")
print(f"\nМаксимальный среди минимальных: {max_of_mins[0]}")
print(f"Индекс найденного элемента: ({max_of_mins[1] + 1}, {max_of_mins[2] + 1})")
print(f"Нумерация с 1: строка {max_of_mins[1] + 1}, столбец {max_of_mins[2] + 1}")
