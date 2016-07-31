'''
Created on Apr 8, 2016

@author: airings
'''
import unittest


class SimpleTestCase(unittest.TestCase):
    '''4444444444'''
    def test_1(self):
        assert 1==2
        
    def test_2(self):
        '''jfdgkjsfdkjgfkdj'''
        x = 1 +2
        assert x==2
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTestCase)
    re = unittest.TextTestRunner(verbosity=2).run(suite)
#     print type(re)
#     print re
#     print re.errors
    print re.failures
#     print re.testsRun
#     print re.wasSuccessful()
    print re.descriptions
#     print re.getDescription(SimpleTestCase)