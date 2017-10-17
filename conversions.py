#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 6, Conversions Module"""


def convertCelsiusToKelvin(ctemp):
    """Takes in a float representing a Celsius temperature, and returns that temperature converted into Kelvins"""
    float(ctemp)
    Ktemp = ctemp + 273.15
    float(Ktemp)
    return round(Ktemp, 2)


def convertCelsiusToFahrenheit(ctemp):
    """Takes in a float representing a Celsius temperature, and returns that temperature converted into Fahrenheit"""
    float(ctemp)
    ftemp = (ctemp*9/5 + 32)
    float(ftemp)
    return round(ftemp, 2)

def convertFahrenheitToCelsius(ftemp):
    """Takes in a float representing a Fahrenheit temperature, and returns that temperature converted into Celsius"""
    float(ftemp)
    ctemp = (ftemp-32)*5/9
    float(ctemp)
    return round(ctemp, 2)

def convertFahrenheitToKelvin(ftemp):
    """Takes in a float representing a Fahrenheit temperature, and returns that temperature converted into Kelvin"""
    float(ftemp)
    ktemp = (ftemp + 459.67)*5/9
    float(ktemp)
    return round(ktemp, 2)

def convertKelvinToFahrenheit(ktemp):
    """Takes in a float representing a Kelvin temperature, and returns that temperature converted into Fahrenheit"""
    float(ktemp)
    ftemp = (ktemp*9/5) - 459.67
    float(ftemp)
    return round(ftemp, 2)

def convertKelvinToCelsius(ktemp):    
    """Takes in a float representing a Kelvin temperature, and returns that temperature converted into Celsius"""
    float(ktemp)
    ctemp = ktemp - 273.15
    float(ctemp)
    return round(ctemp, 2)

def main():
    pass

if __name__ == "__main__":
    main()
