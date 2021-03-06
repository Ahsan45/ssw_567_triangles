import unittest
import Shahab_Ahsan_HW1

class TestTriangles(unittest.TestCase):
    def test_right_scalene(self):
        self.assertEqual(Shahab_Ahsan_HW1.classify_triangle(3,4,5), "Right Scalene")
    
    # new test cases below
    def test_right_scalene2(self):
        self.assertEqual(Shahab_Ahsan_HW1.classify_triangle(5,4,2), "Scalene")

    def test_right_scalene3(self):
        self.assertEqual(Shahab_Ahsan_HW1.classify_triangle(5,7,3), "Scalene")
    # end of new test cases
    
    def test_right_equilateral(self):
        self.assertNotEqual(Shahab_Ahsan_HW1.classify_triangle(5, 5, 5), "Right Equilateral")

    def test_right_isosceles(self):
        self.assertEqual(Shahab_Ahsan_HW1.classify_triangle(12, 12, 15), "Isosceles")

    def test_equilateral(self):
        self.assertEqual(Shahab_Ahsan_HW1.classify_triangle(5, 5, 5), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(Shahab_Ahsan_HW1.classify_triangle(8, 8, 10), "Isosceles")

    def test_scalene(self):
        self.assertEqual(Shahab_Ahsan_HW1.classify_triangle(13, 15, 23), "Scalene")

if __name__ == '__main__':
    unittest.main()