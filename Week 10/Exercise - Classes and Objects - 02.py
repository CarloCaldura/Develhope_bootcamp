class Animal:
    def __init__(self, runs, number_of_legs):
        self.runs = runs
        self.number_of_legs = number_of_legs
    def count_legs(self):
        print(self.number_of_legs)
    def return_legs(self):
        return self.number_of_legs

dog = Animal(number_of_legs = 4, 
                runs = 'Running started')

print(dog.number_of_legs)
