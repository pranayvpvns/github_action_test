import unittest
from app.calculator import add, subtract,multiply,division

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        
    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
    
    def test_division(self):
        self.assertEqual(division(10, 5), 2)

if __name__ == "__main__":
    unittest.main()
