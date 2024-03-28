def factorize(x):
    """ 
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    pass


import unittest

class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        for x in ['string', 1.5]:
            with self.subTest(x=x):
                with self.assertRaises(TypeError):
                    factorize(x)
    
    def test_negative(self):
        
        for x in [-1, -10, -100]:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    factorize(x)
        
            
    def test_zero_and_one_cases(self):
        test_cases = {
            0: (0,),
            1: (1,)
        }
        for number, expected_factors in test_cases.items():
            with self.subTest(number=number):
                self.assertEqual(factorize(number), expected_factors)
        
    def test_simple_numbers(self):
        test_cases = {
            3: (3,),
            13: (13,),
            29: (29,)
        }
        for number, expected_factors in test_cases.items():
            with self.subTest(number=number):
                self.assertEqual(factorize(number), expected_factors)
        
    def test_two_simple_multipliers(self):
        test_cases = {
            6: (2, 3),
            26: (2, 13),
            121: (11, 11)
        }
        for number, expected_factors in test_cases.items():
            with self.subTest(number=number):
                self.assertEqual(factorize(number), expected_factors)
        
    def test_many_multipliers(self):
        test_cases = {
            1001: (7, 11, 13),
            9699690: (2, 3, 5, 7, 11, 13, 17, 19)
        }
        
        for number, expected_factors in test_cases.items():
            with self.subTest(number=number):
                self.assertEqual(factorize(number), expected_factors)

if __name__ == '__main__':
    unittest.main()
       
