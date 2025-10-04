M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
B = []
print("Введите элементы матрицы построчно:")
for i in range(M):
    row = list(map(int, input(f"Строка {i + 1}: ").split()))
    B.append(row)
min_array = [min(B[i][j] for i in range(M)) for j in range(N)]
print("\nИсходная матрица:")
for row in B:
    print(row)
print(f"\nМассив минимальных элементов каждого столбца: {min_array}")
