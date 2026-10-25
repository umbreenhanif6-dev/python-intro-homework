set_a = {'HTML', 'SQL', 'CSS', 'JavaScript', 'Python'}
set_b = {'SQL', 'Python', 'C', 'C++', 'JavaScript'} 

# The union (all languages from both lists, no duplicates) 
print(f"The union of the two sets is: { ', '.join(set_a.union(set_b))}.")

# The intersection (languages in both lists)
print(f"Languages that are common in both lists are: { ', '.join(set_a.intersection(set_b))}.")

#The difference (languages only in the first list)
print(f"Languages found only in the first list are: { ', '.join(set_a.difference(set_b))}.") 