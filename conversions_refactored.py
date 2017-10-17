
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6, Part IV, Conversions Refactored Module"""


def convert(fromUnit, toUnit, value):
    """temperature and distance conversion function, 
       fromUnit and toUnit may be Kelvin, Fahrenheit, or Celsius, meter, yard, or mile, and value to convert,
       value is the temperature to convert"""

    float(value)

    if fromUnit == 'Kelvin' and toUnit == 'Celsius':
        result = value - 273.15
    elif fromUnit == 'Celsius' and toUnit == 'Kelvin':
        result = value + 273.15
    elif fromUnit == 'Celsius' and toUnit == 'Fahrenheit':
        result = (value*9/5) +32
    elif fromUnit == 'Fahrenheit' and toUnit == 'Celsius':
        result = (value-32)*5/9
    elif fromUnit == 'Fahrenhiet' and toUnit == 'Kelvin':
        result = (value+459.67)*5/9
    elif fromUnit == 'Kelvin' and toUnit == 'Fahrenheit':
        result = (value*9/5) - 459.67

    elif fromUnit == 'Fahrenhiet' and toUnit == 'Fahrenheit':
        return value
    elif fromUnit == 'Kelvin' and toUnit == 'Kelvin':
        result = value
    elif fromUnit == 'Celsius' and toUnit == 'Celsius':
        result = value
    elif fromUnit == 'meters' and toUnit == 'meters':
        result = value
    elif fromUnit == 'miles' and toUnit == 'miles':
        result = value
    elif fromUnit == 'yards' and toUnit == 'yards':
        result = value

    elif fromUnit == 'yards' and toUnit == 'meters':
        result = value/1.0936
    elif fromUnit == 'yards' and toUnit == 'miles':
        result = value/1760
    elif fromUnit == 'meters' and toUnit == 'yards':
        result = value*1.0936
    elif fromUnit == 'meters' and toUnit == 'miles':
        result = value*0.00062137
    elif fromUnit == 'miles' and toUnit == 'meters':
        result = 0.00062137/value
    elif fromUnit == 'miles' and toUnit == 'yards':
        result = value*1760

    return value, fromUnit, "is equal to", round(result, 2), toUnit

def main():
    pass

if __name__ == "__main__":
    unittest.main()
