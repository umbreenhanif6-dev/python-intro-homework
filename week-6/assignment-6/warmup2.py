"""
Warmup 2: Functions that Return Values
Write two functions:
·celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
·fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
Call each with a few test values and print the results. Use f-strings and round to one decimal place.
"""
def celsius_to_fahrenheit(C):
    fahrenheit =  (C * 9/5) + 32
    print(f"{C}°C = {fahrenheit:.1f}°F")
    return fahrenheit

def fahrenheit_to_celsius(F):
    celsius = (F - 32) * 5/9
    print( f"{F}°F = {celsius:.1f}°C")
    return celsius 

celsius_to_fahrenheit(12)
celsius_to_fahrenheit(5)
fahrenheit_to_celsius(66)
fahrenheit_to_celsius(79)