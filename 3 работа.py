M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
matrix = []
print("Введите элементы матрицы построчно:")
for i in range(M):
    row = list(map(float, input(f"Строка {i + 1}: ").split()))
    matrix.append(row)
min_value = matrix[0][0]
max_value = matrix[0][0]
min_row = 0
max_row = 0
for i in range(M):
    for j in range(N):
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_row = i
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_row = i
print(f"\nМинимальный элемент: {min_value} (строка {min_row + 1})")
print(f"Максимальный элемент: {max_value} (строка {max_row + 1})")
if min_row != max_row:
    matrix[min_row], matrix[max_row] = matrix[max_row], matrix[min_row]
    print("Строки успешно поменяны местами!")
else:
    print("Минимальный и максимальный элементы находятся в одной строке - замена не требуется.")
print("\nРезультирующая матрица:")
for i in range(M):
    print(f"Строка {i + 1}: {matrix[i]}")
