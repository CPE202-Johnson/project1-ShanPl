import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    
    #additional random number conversions with other bases
    def test_base5(self):
        self.assertEqual(convert(123456,5), "12422311")
    
    def test_base15(self):
        self.assertEqual(convert(9876543210,15), "3CC123290")
    
    def test_base9(self):
        self.assertEqual(convert(9876543210,9), "27438411220")

if __name__ == "__main__":
        unittest.main()