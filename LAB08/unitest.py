#Michaela Jankulicova
#DD1320
#Laboration 8


import unittest
from molekyl_2 import*

class TestStringMethods(unittest.TestCase):

    def test_syntax(self):
        self.assertEqual(check_syntax('H2'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('P21'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('Ag3'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('H10100'), "Formeln är syntaktiskt korrekt")
        
        self.assertEqual(check_syntax('a'), "Saknad stor bokstav vid radslutet a")
        self.assertEqual(check_syntax('cr12'), "Saknad stor bokstav vid radslutet cr12")
        self.assertEqual(check_syntax('8'), "Saknad stor bokstav vid radslutet 8")
        self.assertEqual(check_syntax('H01011'), "För litet tal vid radslutet 1011")

        self.assertEqual(check_syntax('H010'), "För litet tal vid radslutet 10")
        self.assertEqual(check_syntax('H110'), "Formeln är syntaktiskt korrekt")


if __name__ == '__main__':
    unittest.main()