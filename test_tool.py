import unittest
from tool import proportion_interval
class Tests(unittest.TestCase):
 def test_interval(self): self.assertEqual(proportion_interval(50,100),(0.402,0.598))
if __name__=='__main__': unittest.main()
