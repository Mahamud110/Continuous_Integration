import unittest
from Add import *

class TestFunction(unittest.TestCase):
    def test_addition(self):
        result = add(3,5)
        self.assertEqual(result,8)

    def test_addition_neg(self):
        result = add(-2,7)
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()



