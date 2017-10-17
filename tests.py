#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6, Part I, Unit Testing Module which tests values in conversions.py"""

import unittest
import conversions


class ConversionsTesting(unittest.TestCase):
                     
    ctokvalues = ((-89.2, 183.95),
                    (-17.78, 255.37),
                    (0, 273.15),
                    (15, 288.15),
                    (37, 310.15))

    def testCtoK(self):                          
        """tests that convertCelsiusToKelvin returns the correct values"""
        print 'tests that convertCelsiusToKelvin returns the correct values'
        for integer, numeral in self.ctokvalues:
            result = conversions.convertCelsiusToKelvin(integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

                          
    ctofvalues = ((50, 122),
                    (40, 104),
                    (0, 32),
                    (-10, 14),
                    (30, 86))

    def testCtoF(self):                          
        """tests that convertCelsiusToFahrenheit returns the correct values"""
        print 'tests that convertCelsiusToFahrenheit returns the correct values'
        for integer, numeral in self.ctofvalues:
            result = conversions.convertCelsiusToFahrenheit(integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')


    ftocvalues = ((932, 500),
                    (68, 20),
                    (32, 0),
                    (50, 10),
                    (14, -10))

    def testFtoC(self):                          
        """tests that convertFahrenheitToCelsius returns the correct values"""
        print 'tests that convertFahrenheitToCelcius returns the correct values'
        for integer, numeral in self.ftocvalues:
            result = conversions.convertFahrenheitToCelsius(integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')


    ftokvalues = ((932, 773.15),
                    (158, 343.15),
                    (32, 273.15),
                    (-4, 253.15),
                    (14, 263.15))

    def testFtoK(self):                          
        """tests that convertFahrenheitToKelvin returns the correct values"""
        print 'tests that convertFahrenheitToKelvin returns the correct values'
        for integer, numeral in self.ftokvalues:
            result = conversions.convertFahrenheitToKelvin(integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')


    ktofvalues = ((773.15, 932),
                    (343.15, 158),
                    (273.15, 32),
                    (253.15, -4),
                    (263.15, 14))

    def testKtoF(self):                          
        """tests that convertKelvinToFahrenheit returns the correct values"""
        print 'tests that convertKelvinToFahrenheit returns the correct values'
        for integer, numeral in self.ktofvalues:
            result = conversions.convertKelvinToFahrenheit(integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    ktocvalues = ((773.15, 500),
                    (343.15, 70),
                    (273.15, 0),
                    (253.15, -20),
                    (263.15, -10))

    def testKtoC(self):                          
        """tests that convertKelvinToCelsius returns the correct values"""
        print 'tests that convertKelvinToCelsius returns the correct values'
        for integer, numeral in self.ktocvalues:
            result = conversions.convertKelvinToCelsius(integer)                    
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')



if __name__ == "__main__":
    unittest.main()   
