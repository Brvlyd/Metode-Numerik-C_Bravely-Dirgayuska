import numpy as np

def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        print("Matriks tidak memiliki balikan.")
        return None

# Testing
matrix = np.array([[1, 2], [3, 4]])
inv_matrix = inverse_matrix(matrix)

if inv_matrix is not None:
    print("Matriks asli:")
    print(matrix)
    print("Matriks balikan:")
    print(inv_matrix)
