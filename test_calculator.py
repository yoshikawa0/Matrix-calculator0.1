
import unittest
from calculator import MatrixCalculator

class TestMatrixCalculator(unittest.TestCase):
    def test_add_matrices(self):
        calc = MatrixCalculator()
        result = calc.add_matrices([[1, 2]], [[3, 4]])
        self.assertEqual(result, [[4, 6]])

    def test_multiply_matrices(self):
        calc = MatrixCalculator()
        result = calc.multiply_matrices([[1, 2]], [[3], [4]])
        self.assertEqual(result, [[11]])

    def test_transpose_matrix(self):
        calc = MatrixCalculator()
        result = calc.transpose_matrix([[1, 2], [3, 4]])
        self.assertEqual(result, [[1, 3], [2, 4]])

if __name__ == "__main__":
    unittest.main()
