"""
Warmup 3: Scope in Action
Demonstrate variable scope with two short examples in one file:
1.Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then 
remove or comment out the line that causes it.
2.Show how return solves the problem: return the value from the function and assign it to a 
variable in the outer scope. Print it to confirm it worked.
Save as: warmup3.py
"""
def area_triangle(base, height):
    triangle = 0.5 * base * height 
    print(triangle)
area_triangle(5, 6)
# print(triangle)

"""
Traceback (most recent call last):
  File "c:\Umbreen\python-intro-homework\week-6\assignment-6\warmup3.py", line 14, in <module>
    print(triangle)
          ^^^^^^^^
NameError: name 'triangle' is not defined
"""

# show how return solves the problem
def area_triangle(base, height):
    triangle = 0.5 * base * height 
    return triangle

result = area_triangle(5, 6)

print(result)