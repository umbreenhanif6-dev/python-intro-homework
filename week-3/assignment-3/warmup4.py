<<<<<<< HEAD
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
=======
# Write a script that evaluates the five expressions below and prints each one with its result. 
# Add a comment on each line explaining why the result is what it is:
print(not True and False) 
#Result is False because in and statements, both values must be logically true or logically false.  
print(True or False and False)
# Result is True because 'and' operator takes priority over 'or', therefore 
# Python reads the script as ('False and False) first, then 'True or (False)' 
print(not (5 > 3))
#False is printed because 'not' operator is changing the value (True) of the statement '5 > 3'
#  into not (True) which is incorrect, and therefore False
print(10 == 10 and 4 != 4)
#False is printed because both arguments must be logically true in order to return
#  True output for 'and' operator. Second argument is logically false 
print(not False or not True)
# True is output because the statement is basically saying true or
# false. When the 'or' operator is present, one condition must be true in order to 
# have a 'True' output
>>>>>>> 78481ff (add warmup3 for assignment 3)
