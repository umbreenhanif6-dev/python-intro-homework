numbers = [42, 17, 83, 5, 61, 29, 74, 8, 
           55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_max(numbers):
    max_num = numbers[0]    
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def search(numbers, target):
    for index, num in enumerate(numbers):
        if target == num:
            return index
    else: 
        return -1

def bubble_sort(numbers):
    sorted_numbers = numbers [:]
    swapped = True
    while swapped:
            swapped = False
            for num in range(len(sorted_numbers) -1):
                if sorted_numbers[num] > sorted_numbers[num + 1]: 
                    sorted_numbers[num], sorted_numbers[num + 1] = sorted_numbers[num + 1],    sorted_numbers[num]
                    swapped = True 
    return sorted_numbers [:]

def show_menu(): 

    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    option = input("Select an option from the menu: ")
    return option

def main()