#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6, Part I, Unit Testing Module which tests values in conversions.py"""

import unittest
import conversions_refactored


class ConversionsTesting(unittest.TestCase):
                     
    ctokvalues = ((-89.2, 183.95),
                    (-17.78, 255.37),
                    (0, 273.15),
                    (15, 288.15),
                    (37, 310.15))

    def testCtoK(self):                          
        """tests that convertCelsiusToKelvin returns the correct values"""
        for integer, numeral in self.ctokvalues:
            result = conversions_refactored.convert('Celsius', 'Kelvin', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

                          
    ctofvalues = ((50, 122),
                    (40, 104),
                    (0, 32),
                    (-10, 14),
                    (30, 86))

    def testCtoF(self):                          
        """tests that convertCelsiusToFahrenheit returns the correct values"""
        for integer, numeral in self.ctofvalues:
            result = conversions_refactored.convert('Celsius', 'Fahrenheit', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')


    ftocvalues = ((932, 500),
                    (68, 20),
                    (32, 0),
                    (50, 10),
                    (14, -10),
                    (14, 14))

    def testFtoC(self):                          
        """tests that convertFahrenheitToCelsius returns the correct values"""
        for integer, numeral in self.ftocvalues:
            result = conversions_refactored.convert('Fahrenheit', 'Celsius', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')


    ftokvalues = ((932, 773.15),
                    (158, 343.15),
                    (32, 273.15),
                    (-4, 253.15),
                    (14, 263.15))

    def testFtoK(self):                          
        """tests that convert returns the correct Fahrenheit To Kelvin values"""
        for integer, numeral in self.ftokvalues:
            result = conversions_refactored.convert('Fahrenheit', 'Kelvin', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')


    ktofvalues = ((773.15, 932),
                    (343.15, 158),
                    (273.15, 32),
                    (253.15, -4),
                    (263.15, 14))

    def testKtoF(self):                          
        """tests that convert returns the correct Kelvin To Fahrenheit values"""
        for integer, numeral in self.ktofvalues:
            result = conversions_refactored.convert('Kelvin', 'Fahrenheit', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    ktocvalues = ((773.15, 500),
                    (343.15, 70),
                    (273.15, 0),
                    (253.15, -20),
                    (263.15, -10))

    def testKtoC(self):                          
        """tests that convert returns the correct Kelvin To Celsius values"""
        for integer, numeral in self.ktocvalues:
            result = conversions_refactored.convert('Kelvin', 'Celsius', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    mettoyvalues = ((5.49, 6),
                    (6.40, 7),
                    (18.29, 20))

    def testMettoY(self):
        """docstring"""
        for integer, numeral in self.mettoyvalues:
            result = conversions_refactored.convert('meters', 'yards', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    ytometvalues = ((6, 5.49),
                    (7, 6.40),
                    (20, 18.29))

    def testYtoMet(self):
        """docstring"""
        for integer, numeral in self.ytometvalues:
            result = conversions_refactored.convert('yards', 'meters', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    mitoyvalues = ((1, 1760),
                    (4, 7040),
                    (6, 10560))

    def testMitoY(self):
        """docstring"""
        for integer, numeral in self.mitoyvalues:
            result = conversions_refactored.convert('miles', 'yards', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    ytomivalues = ((1760, 1),
                   (7040, 4),
                   (10560, 6))

    def testYtoMi(self):
        """docstring"""
        for integer, numeral in self.ytomivalues:
            result = conversions_refactored.convert('yards', 'miles', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    mitometvalues = ((2, 3218.69),
                     (9, 14484.10),
                     (6, 9656.06))

    def testMitoMet(self):
        """docstring"""
        for integer, numeral in self.mitometvalues:
            result = conversions_refactored.convert('miles', 'meters', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    mettomivalues = ((3218.69, 2),
                     (14484.10, 9),
                     (9656.06, 6))

    def testMettoMi(self):
        """docstring"""
        for integer, numeral in self.mettomivalues:
            result = conversions_refactored.convert('meters', 'miles', integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

def main():
    pass

if __name__ == "__main__":
    unittest.main()
