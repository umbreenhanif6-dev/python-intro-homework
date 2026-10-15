x = int(input("Enter a number: "))

if x < 0: 
	print(f"{x} is a negative number.") 
elif x > 0:
	print(f"{x} is a positive number.")
else: print("0 is zero. ")

if x % 2 == 0: 
	print("The number is even. ")
else: 
	print("The number is odd. ")