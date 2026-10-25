"""""
Warmup 1: List Operations
Create a hardcoded list of 8 numbers. Without using any loops, print:
1.The first item
2.The last item (use a negative index)
3.A slice containing only the middle four items
4.The full list in reverse order
"""""

alist = [34, 76, 89, 345, 90, 27, 786, 129]
# The first item
print(f"The first item is {alist[0]}.") 	
# The last item (use a negative index)
print(f"The last item is {alist[-1]}.") 		 
# A slice containing only the middle four items
print(f"The middle four items are {alist[2:6]}.")	
# The full list in reverse order
print(f"The full list in reverse order is {alist[::-1]}.")	    