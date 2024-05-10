def crout_decomposition(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for j in range(n):
        U[j][j] = 1.0

        for i in range(j, n):
            sum_l = sum(L[i][k] * U[k][j] for k in range(i))
            L[i][j] = matrix[i][j] - sum_l

        for i in range(j+1, n):
            sum_u = sum(L[j][k] * U[k][i] for k in range(j))
            U[j][i] = (matrix[j][i] - sum_u) / L[j][j]

    return L, U

# Testing
A = [[4, 3, -2], [2, 1, 1], [8, 9, 3]]
L, U = crout_decomposition(A)
print("Matriks L:")
for row in L:
    print(row)
print("Matriks U:")
for row in U:
    print(row)
