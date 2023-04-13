from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def makeASound(self)->str:
        pass

class Doggie(Animal):
    def makeASound(self):
        return 'Woof!'
    

class Cat(Animal):
    def makeASound(self):
        return 'Meow!' 


class Cow(Animal):
    def makeASound(self):
        return 'Moo!'        
    
dog = Doggie()
cat = Cat()
cow = Cow()

animals: list[Animal] = [dog,cat,cow]

for animal in animals:
    print(animal.makeASound())

