import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_false(self):
        #cannot win by starting with less than 42 if only giving back bears
        self.assertFalse(bears(0))
        self.assertFalse(bears(-1))
        self.assertFalse(bears(3))
        for i in range(41):
            self.assertFalse(bears(i))
        self.assertFalse(bears(300))
    
if __name__ == "__main__":
    unittest.main()
