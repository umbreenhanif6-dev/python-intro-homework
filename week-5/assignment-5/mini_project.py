"""
Build a menu-driven program using a while loop. Each time the menu displays, the user picks an option.
 The menu below shows the format — your wording and layout might differ, but all five options must be present:

=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5):

"""
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 
           55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
select = " "

while select != "5":
    print("\n=== Number Games ===")
    print("1. Find the smallest number")
    print("2. Find the largest number")
    print("3. Search for a number")
    print("4. Sort the list  from lowest to highest value")
    print("5. Quit")
    select = input("Choose an option (1-5): ")

    if select == "1":
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        print(f"\nThe smallest number in the list is {min_num}.\n")

    elif select == "2":
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        print(f"\nThe largest number in the list is {max_num}.\n")

    elif select == "3":
        guess = int(input("\nEnter a number to search for: "))
        if guess in numbers:
            print(f"{guess} is in the list.\n")
        else:
            print(f"{guess} is not in the list.\n")

    elif select == "4":
        swapped = False

        while swapped:
            swapped = False
            for num in range(len(numbers) -1):
                if numbers[num] > numbers[num + 1]:
                    numbers[num], numbers[num + 1] = numbers[num + 1], numbers[num]
                    swapped = True 
                print(f"\nThe list has been sorted from lowest to highest value: {numbers}\n")

    elif select == "5":
        print("\nExiting the program. Goodbye!\n")

    else:
        print("\nInvalid option. Please choose a number between 1 and 5.\n")


