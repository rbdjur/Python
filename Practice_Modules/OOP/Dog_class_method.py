class Dog():
    #Object attributes 
    species = 'Mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    
    #Methods / Operations
    def bark(self, number):
        print(f"Woof my name is {self.name}. the number is {number}")


my_dog = Dog("lab", "Happy", False)

# print(my_dog.bark())
 
print(f"{my_dog.bark(10)}.  He is a {my_dog.breed}. Does he have spots, you ask? {my_dog.spots}. Oh by the way he is a {my_dog.species}")

