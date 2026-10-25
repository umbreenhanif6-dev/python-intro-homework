set_a = {'html', 'sql', 'css', 'javascript', 'python'}
set_b = {'sql', 'python', 'c', 'c++', 'javascript'} 

# The union (all languages from both lists, no duplicates) 
print(set_a.union(set_b)) 

# The intersection (languages in both lists)
print(set_a.intersection(set_b)) 

#The difference (languages only in the first list)
print(set_a.difference(set_b)) 