<<<<<<< HEAD
"""""
Warmup 3: Set Operations
Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:
1.The union (all languages from both lists, no duplicates)
2.The intersection (languages in both lists)
3.The difference (languages only in the first list)
"""""
=======
>>>>>>> 1722116ca6720722d49f7ab76d18c3acd0052c94
set_a = {'html', 'sql', 'css', 'javascript', 'python'}
set_b = {'sql', 'python', 'c', 'c++', 'javascript'} 

# The union (all languages from both lists, no duplicates) 
<<<<<<< HEAD
print(f"All the languages in the list are: {', '.join(set_a.union(set_b))}")

# The intersection (languages in both lists)
print(f"The languages in both lists are: {', '.join(set_a.intersection(set_b))}")

#The difference (languages only in the first list)
print(f"The languages only in the first list are: {', '.join(set_a.difference(set_b))}")
=======
print(set_a.union(set_b)) 

# The intersection (languages in both lists)
print(set_a.intersection(set_b)) 

#The difference (languages only in the first list)
print(set_a.difference(set_b)) 
>>>>>>> 1722116ca6720722d49f7ab76d18c3acd0052c94
