"""""
Warmup 1: List Operations
Create a hardcoded list of 8 numbers. Without using any loops, print:
1.The first item
2.The last item (use a negative index)
3.A slice containing only the middle four items
4.The full list in reverse order
"""""

alist = [34, 76, 89, 345, 90, 27, 786, 129]

print(alist[0]) 		# The first item
print(alist[-1]) 		# The last item (use a negative index)
print(alist[2:6])		# A slice containing only the middle four items
print(alist[::-1])	    # The full list in reverse order
