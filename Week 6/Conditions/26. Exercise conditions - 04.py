'''Exercise Conditions - 4
Compare those 2 numbers' absolute values and write X's absolute value greater than Y's absolute value Use abs function to do that
eg.
abs(-5) -> 5
abs function makes all numbers positive'''

import random

number1 = random.randint(-100,100)
number2 = random.randint(-100,100)
print(f"number1 = {number1} and number2 = {number2}")
if abs(number1) > abs(number2):
    print(f"Absolute value of {number1} is greater than absolute value of {number2}")
elif abs(number2) > abs(number1):
    print(f"Absolute value of {number2} is greater than absolute value of {number2}")
else:
    print(f"Absolute value of {number1} is equal to absolute value of {number2}")