'''
In this exercise, you’ll define a class, Scoop, that represents a single scoop of ice cream. 
Each scoop should have a single attribute, flavor, 
a string that you can initialize when you create the instance of Scoop. 
Once your class is created, write a function (create_scoops) that creates three instances of the Scoop class, 
each of which has a different flavor. 
Put these three instances into a list called scoops. 
Finally, iterate over your scoops list, printing the flavor.
'''

class Scoop:
    def __init__(self, flavour):
        self.flavour = flavour

def create_scoops():
    
    scoops = [Scoop('vanilla'), Scoop('chocolate'), Scoop('cream')]

    for scoop in scoops:
        print(scoop.flavour)

create_scoops()