#Exercise Methods - 2
#the number types can be converted to each other wit the int() float() complex() methods also float numbers can be rounded with the method round()

'''convert num1 to float and assign to itself
convert num2 to int and assign to itself
convert num3 to complex and assign to itself
use round method for num4 and assign to itself
use round method for num5 and assign to itself
print them all
print their types'''

num1 = float(1.3)
num2 = int(2.3)
num3 = complex(1j) 
num4 = round(1.4) 
num5 = round(1.5)

for num in (num1, num2, num3, num4, num5):
    print(f"{num} : {type(num)}")