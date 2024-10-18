import unittest
from Add import *

class TestFunction(unittest.TestCase):
    def test_addition(self):
        result = add(3,6)
        self.assertEqual(result,9)

    def test_addition_neg(self):
        result = add(-2,7)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()



