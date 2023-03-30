my_list= [*range(5)]
for i in my_list:
    f = lambda x : x*x
    if (f(i)%2) == 0:
        print(f(i))

