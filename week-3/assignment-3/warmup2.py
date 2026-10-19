age = int(input("Please enter your age: "))
if age <0:
    print("Please check your answer. ")
elif age <= 12:
	print("You are a Child.")
elif age >= 13 and age  <= 17:
	print("You are a Teen.")
elif age >= 18 and age  <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")