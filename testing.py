

import unittest
from unittest import result
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 5), 4)
    
    def test_sub(self):
        self.assertEqual(calc.substract(10, 5), 10)
        self.assertEqual(calc.add(-1, 5), 4)


    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 5), 4)


if __name__ == "__main__":
    unittest.main()