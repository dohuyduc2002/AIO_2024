from unittest import result
import numpy as np

def compute_vector_length(vector):
    arr = np.array(vector)
    len_of_vector = np.linalg.norm(arr)
    return len_of_vector

def compute_dot_product(vector1,vector2):
    arr1 = np.array(vector1)
    arr2 = np.array(vector2)
    result = np.dot(arr1,arr2)
    return result

def matrix_mul_vector(matrix,vector):
    #broadcasting only work with vector with shape (1,)
    mat = np.array(matrix)
    vec = np.array(vector)
    c = np.dot(mat,vec)
    return c 

def inverse_matrix(matrix):
    return np.linalg.inv(matrix)

def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    eigenvectors = eigenvectors / np.linalg.norm(eigenvectors, axis=0)
    return eigenvalues, eigenvectors

def compute_cosine(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


