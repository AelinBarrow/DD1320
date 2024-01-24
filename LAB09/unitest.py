
#DD1320
#Laboration 8


import unittest
from molekylV12 import*

class TestStringMethods(unittest.TestCase):

    def test_syntax_input1(self):
        self.assertEqual(check_syntax('H'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('Na'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('H2O'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('Si(C3(COOH)2)4(H2O)7'), "Formeln är syntaktiskt korrekt")
        self.assertEqual(check_syntax('Na332'), "Formeln är syntaktiskt korrekt")
        
    def test_syntax_input2(self):
        self.assertEqual(check_syntax('C(Xx4)5'), "Okänd atom vid radslutet 4)5")
        self.assertEqual(check_syntax('C(OH4)C'), "Saknad siffra vid radslutet C")
        self.assertEqual(check_syntax('C(OH4C'), "Saknad högerparentes vid radslutet ")
        self.assertEqual(check_syntax('H2O)Fe'), "Felaktig gruppstart vid radslutet )Fe")
        self.assertEqual(check_syntax('H0'), "För litet tal vid radslutet ")
        self.assertEqual(check_syntax('H1C'), "För litet tal vid radslutet C")
        self.assertEqual(check_syntax('H02C'), "För litet tal vid radslutet 2C")
        self.assertEqual(check_syntax('Nacl'), "Saknad stor bokstav vid radslutet cl")

        self.assertEqual(check_syntax('a'), "Saknad stor bokstav vid radslutet a")
        self.assertEqual(check_syntax('(Cl)2)3'), "Felaktig gruppstart vid radslutet )3")
        self.assertEqual(check_syntax(')'), "Felaktig gruppstart vid radslutet )")
        self.assertEqual(check_syntax('2'), "Felaktig gruppstart vid radslutet 2")

    def test_syntax_input3(self):
        self.assertEqual(check_syntax('A'), "Okänd atom vid radslutet ")
        self.assertEqual(check_syntax('F'), "Formeln är syntaktiskt korrekt")
        
if __name__ == '__main__':
    unittest.main()
