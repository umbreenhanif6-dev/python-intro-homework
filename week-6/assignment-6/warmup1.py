"""Warmup 1: Default Parameters
Write a function greet(name, greeting="Hello") that prints a greeting. 
Call it three different ways:
"""

#1. With only a name argument

def greet(name, greeting="Hello"):
    print(greeting + " " + name + "!")
greet("Abdul")

# 2. With both a name and a custom greeting
def greet(name, greeting):
    print(name +  ", " +  greeting)
greet("Zainab", "How are you today?")
# 3. With the greeting passed as a keyword argument

def greet(name, greeting):
    print(greeting + " " + name + ".")
greet("Abdul" ,  greeting= "Hello")