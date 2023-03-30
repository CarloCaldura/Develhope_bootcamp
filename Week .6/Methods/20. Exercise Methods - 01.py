#With type command you can see the type of a variable in python eg: 
#type(1) print each components type with this way you can see most significant data types in python

__ = type

print(__("Hello World"))
print(__(True))
print(__(False))
print(__(33))
print(__(24.5))
print(__(4+1j))
print(__(4j))
print(__(["lion", "monkey", "dog","fish"]))
print(__(("lion", "monkey", "dog","fish")))
print(__({"name" : "John", "surname" : "Doe", "age":22}))
print(__({"lion", "monkey", "dog","fish"}))