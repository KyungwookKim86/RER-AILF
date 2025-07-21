import numpy as np

def estimate_position(A_matrix, b_vector, weights):
    W = np.diag(weights)
    ATA_inv = np.linalg.inv(A_matrix.T @ W @ A_matrix)
    return ATA_inv @ A_matrix.T @ W @ b_vector