"""
Warmup 4: FizzBuzzSave as: warmup4.py
Loop from 1 to 30 and print one word per line:
·"FizzBuzz" if the number is divisible by both 3 and 5
·"Fizz" if divisible by 3 only
·"Buzz" if divisible by 5 only
·The number itself otherwise
Check the combined case first.
"""
numbers = range( 1, 31)
for multiple in numbers :
    if multiple % 3 == 0 and multiple % 5 == 0:     
        print("FizzBuzz")
    elif multiple % 3 == 0: 
        print("Fizz")
    elif multiple % 5 == 0:  
        print("Buzz")
    else:
        print(f"{multiple}")
