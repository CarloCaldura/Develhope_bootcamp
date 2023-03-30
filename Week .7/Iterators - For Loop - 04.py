# Iterators - Exercise 4 🐍

'''
iterate each elements of `list1`,`tuple1`,`set1` and print them out 

for the `dict1` iterate all elements but only print the ones who are living on land
in the form of `x lives in y`'''

list1 = ["lion", "monkey", "dog","fish"]
tuple1 = ("lion", "monkey", "dog","fish")
set1 = {"lion", "monkey", "dog","fish"}
dict1 = {"lion":"land", "monkey":"land", "dog":"land","fish":"water"}

for i in list1, tuple1, set1 :
    print(i)
    i =+ 1

for x in dict1 :
    y = dict1[x] 
    if y == "land" :
        print(f"{x} lives in {y}")
    