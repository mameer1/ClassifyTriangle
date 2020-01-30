import unittest
from classifyTriangle import classify_triangle

class triangleTest(unittest.TestCase):
    def testLessArgs(self):
        self.assertEqual(classify_triangle(3), "ERROR: Number of arguments must equal 3")
    def testMoreArgs(self):
        self.assertEqual(classify_triangle(3,4,5,6), "ERROR: Number of arguments must equal 3")
    def testNonInteger(self):
        self.assertEqual(classify_triangle(3,"side",5), "ERROR: Invalid Input(s) -> non-numbers forbidden")
    def testNegative(self):
        self.assertEqual(classify_triangle(3,-4,5), "ERROR: Invalid Input(s) -> negative numbers and zero forbidden")
    def testNonTriangle(self):
        self.assertEqual(classify_triangle(3,4,8), "ERROR: Not a triangle")
    def testEquilateral(self):
        self.assertEqual(classify_triangle(3,3,3), "The triangle is equilateral")
    def testIsoscelesRight(self):
        self.assertEqual(classify_triangle(3,3,3*2**.5), "The triangle is isosceles AND right")
    def testIsosceles(self):
        self.assertEqual(classify_triangle(3,3,5), "The triangle is isosceles")
    def testScaleneRight(self):
        self.assertEqual(classify_triangle(10,24,26), "The triangle is scalene AND right")
    def testScalene(self):
        self.assertEqual(classify_triangle(3,5,6), "The triangle is scalene")
    def testArray(self):
        self.assertEqual(classify_triangle([3],4,5), "ERROR: Invalid Input(s) -> non-numbers forbidden") 

if __name__ == '__main__':
    unittest.main()
