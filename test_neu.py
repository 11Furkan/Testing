import unittest

from neu import multi

class TestMulti(unittest.TestCase):
    
    def Test_multi_function(self):
        self.assertEqual(multi(2,4),8)
        self.assertEqual(multi(2,5),10)

if __name__ == "__main__":
    unittest.main()