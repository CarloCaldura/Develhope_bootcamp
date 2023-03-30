class Animal:
    def __init__(self, runs, leg_count):
        self.runs = runs
        self.leg_count = leg_count

dog = Animal(leg_count='Animal object was created', 
                runs = 'Running started')

print(dog.runs)
