#Reference

# class Dog():
#     #Object attributes 
#     species = 'Mammal'

#     def __init__(self, breed, name, spots):
#         self.breed = breed
#         self.name = name
#         self.spots = spots
    
#     #Methods / Operations
#     def bark(self, number):
#         print(f"Woof my name is {self.name}. the number is {number}")

class Animal ():
    def __init__ (self):
        print("Animal created.")

    def who_am_i (self):
        print("I am an animal.")

    def eating(self):
        print("I am eating.")

# my_animal = Animal()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i (self):
        print("I am a dog.")

my_dog = Dog()

myanimal = Animal()

myanimal.eating()

my_dog.who_am_i()

