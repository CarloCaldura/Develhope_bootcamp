#Implement Fibonacci sequence as recursive function and print first 5 elements.
#use list comprehension while creating the list 
#minimum element is 0 in this series
def fibonacci(n):

    if n in {0, 1}:
         return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(n) for n in range(5)])
