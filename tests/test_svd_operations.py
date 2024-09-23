import unittest
from svd_compression.svd_operations import compute_svd, reconstruct_image
import numpy as np

class TestSVDOps(unittest.TestCase):
    def test_svd_compression(self):
        A = np.random.random((10, 10))
        U, S, Vt = compute_svd(A)
        self.assertEqual(U.shape, (10, 10))
        self.assertEqual(S.shape, (10,))
        self.assertEqual(Vt.shape, (10, 10))

    def test_reconstruct_image(self):
        A = np.random.random((10, 10))
        U, S, Vt = compute_svd(A)
        A_reconstructed = reconstruct_image(U, S, Vt, n_components=5)
        self.assertEqual(A_reconstructed.shape, A.shape)

if __name__ == '__main__':
    unittest.main()
