"""
Ask the user for two numbers. Compute the result of 
dividing the first by the second. Use try/except ZeroDivisionError 
to catch division by zero and print a friendly message instead of crashing.
"""

while True:
    try:
        num = input("Enter a dividend (or type 'exit' to quit): ")
        if num == "exit":
            break
        else:  
            num = int(num)
    except ValueError:
        print("That is not a valid number. Try again.")    
        continue
    while True:
        try:
            div = input("Enter a divisor (or type 'exit' to quit): ")
            if div == "exit":
                break
            else:
                div = int(div)
                result = num / div
        except ValueError:
            print("That is not a valid number. Try again.")
        except ZeroDivisionError: 
            print("You cannot divide by 0.")
            continue
        else:
            print(f"{result:.2f}")
            break
    break