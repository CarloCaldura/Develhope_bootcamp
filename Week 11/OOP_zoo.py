'''For the purposes of these exercises, you are the director of IT at a zoo. 
The zoo contains several different kinds of animals, and for budget reasons, 
some of those animals have to be housed alongside other animals.

We will represent the animals as Python objects, with each species defined as a distinct class. 
All objects of a particular class will have the same species and number of legs, 
but the color will vary from one instance to another.

We’re going to assume that our zoo contains four different types of animals: 
sheep, wolves, snakes, and parrots. 
(The zoo is going through some budgetary difficulties, so our animal collection is both small and unusual.) 
Create classes for each of these types, 
such that we can print each of them and get a report on their color, 
species, and number of legs.'''

class Animal:
    def __init__(self, species, number_of_legs, color):
        self. species = species
        self.number_of_legs = number_of_legs
        self.color = color

    def report_animal(self):
        print(f'This animal is a {self.species}, it has {self.number_of_legs} legs and is {self.color}.')
        
class Sheep(Animal):
    def __init__(self, color):
        super().__init__('sheep', 4, color)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__('wolf', 4, color)

class Snake(Animal):
    def __init__(self, color):
        super().__init__('snake', 0, color)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__('parrot', 2, color)

sheep = Sheep('white')                  
sheep.report_animal()

wolf = Wolf('grey')
wolf.report_animal()

snake = Snake('camouflage')
snake.report_animal()

parrot = Parrot('green')
parrot.report_animal()