M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
B = []
print("Введите элементы матрицы построчно:")
for i in range(M):
    row = list(map(int, input(f"Строка {i + 1}: ").split()))
    B.append(row)
min_array = []
for j in range(N):
    min_val = B[0][j]
    for i in range(1, M):
        if B[i][j] < min_val:
            min_val = B[i][j]
    min_array.append(min_val)
print("\nИсходная матрица:")
for row in B:
    print(row)
print(f"\nМассив минимальных элементов каждого столбца: {min_array}")
