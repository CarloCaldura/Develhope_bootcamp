
class Animal:
    def __init__(self,legs_count):
        print("Animal object was created")
        self.number_of_legs = legs_count

    def runs(self):
        print("Running started")

    def count_legs(self):
        print(f"It has {self.number_of_legs}")

    def return_legs(self):
        return self.number_of_legs
        
class Dog(Animal):
    def __init__(self, name, legs_count):
        super().__init__(legs_count)
        self._name = name

    def bark(self):
        print('woof woof')

    @property
    def get_name(self):
        return self._name
    
shiva = Dog('Shiva', legs_count=4)
print(shiva._name)
shiva.bark()
print(shiva.number_of_legs)

