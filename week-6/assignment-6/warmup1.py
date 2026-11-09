"""Warmup 1: Default Parameters
Write a function greet(name, greeting="Hello") that prints a greeting. 
Call it three different ways:
"""

def greet(name, greeting="Hello"):
    print(greeting + " " + name + "!")
#1. With only a name argument
greet("Abdul")
# 2. With both a name and a custom greeting
greet("Abdul", "How are you today?")
# 3. With the greeting passed as a keyword argument
greet("Abdul", greeting="Hello")
