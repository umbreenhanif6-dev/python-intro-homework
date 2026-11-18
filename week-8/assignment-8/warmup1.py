"""
Write a loop that asks the user to enter a number. If they enter something that can't 
be converted to a number, catch the ValueError with try/except, 
print a message, and ask again. Once you have a valid number, 
print it and stop. The example session below shows the format — your inputs and message wording might differ:
"""


while True:
    try:
        guess = int(input("Enter a number: "))
        print("You entered:", guess)
        break

    except ValueError:
        print("That is not a valid number. Try again.")