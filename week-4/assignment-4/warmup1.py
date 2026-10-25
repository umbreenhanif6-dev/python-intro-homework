alist = [34, 76, 89, 345, 90, 27, 786, 129]
# The first item
print(f"The first item in this list is { ', '.join(str(x) for x in [alist[0]]) }.") 	
# The last item (use a negative index)
print(f"The last item in this list is { ', '.join(str(x) for x in [alist[-1]]) }.") 	
# A slice containing only the middle four items	
print(f"The middle four items in this list are: { ', '.join(str(x) for x in alist[2:6]) }.")	
# The full list in reverse order
print(f"The full list in reverse order is: { ', '.join(str(x) for x in alist[::-1]) }.")	