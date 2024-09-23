import numpy as np

def compute_svd(matrix):
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)
    return U, S, Vt

def reconstruct_image(U, S, Vt, n_components):
    return np.matrix(U[:, :n_components]) * np.diag(S[:n_components]) * np.matrix(Vt[:n_components, :])

def svd_compression(image, n_components):
    U, S, Vt = compute_svd(image)
    compressed_image = reconstruct_image(U, S, Vt, n_components)
    return np.clip(compressed_image, 0, 255).astype(np.uint8)

def compress_color_image(R, G, B, n_components):
    R_compressed = svd_compression(R, n_components)
    G_compressed = svd_compression(G, n_components)
    B_compressed = svd_compression(B, n_components)
    return R_compressed, G_compressed, B_compressed
