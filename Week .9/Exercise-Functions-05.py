import random
list1 = []
def random_list_summer(*a):
   for i in range(0, 15):
      n = random.randint(-100, 100)
      list1.append(n)
   mysum = sum(list1)
   return list1, mysum
   

print(random_list_summer(list1))
      