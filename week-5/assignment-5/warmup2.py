"""
Warmup 2: Input Validation with a While Loop Save as: warmup2.py
Use a while loop that repeatedly asks the user to enter a positive integer.
 If the user enters anything that isn't a positive integer, print a message and ask again.
 Once valid input is received, print it and stop. The example session below shows the format 
 — your inputs and message wording might differ: Hint: You'll need try/except to handle
   non-numeric input — or you can check str.isdigit().
"""

# while True:
#     try:
#         user_input_str = input("Please enter a positive integer: ")
#         if (not user_input_str[0] == "0" or not user_input_str == "0") and user_input_str.isdigit():
#             print(f"\nYou are correct! {user_input_str} is a positive integer!\n")
#             break
#         else:
#             int(user_input_str)
#             print("\nTry another integer.\n")
#     except ValueError:
#         print("Enter a valid integer.")
    
    #     user_input = int(input("Please enter a positive integer: "))
    #     if user_input > 0:
    #         print(f"\nYou are correct! {user_input} is a positive integer!\n")
    #         break
    #     else:
    #         print("\nTry another integer.\n")
    # except ValueError:
    #     print("\nThat was not an integer. Try again.\n")


while True:
    try:
        user_input = int(input("Please enter a positive integer."))
        if user_input > 0: 
            print(f"You are correct!" f"{user_input} is a positive integer!")
            break 
        else: 
            print("Try another integer.")
    except ValueError:
        print("That was not an integer. Try again.")