import numpy as np

def LU_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - sum

        for k in range(i, n):
            if (i == k):
                L[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
                L[k][i] = (A[k][i] - sum) / U[i][i]

    return L, U

# Testing
A = np.array([[4, 3, 2],
              [2, 1, 3],
              [3, 4, 2]])

L, U = LU_decomposition(A)
print("Lower Triangular Matrix (L):")
print(L)
print("\nUpper Triangular Matrix (U):")
print(U)
