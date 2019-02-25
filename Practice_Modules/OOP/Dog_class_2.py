class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = "lab", name = "Sam", spots = False)

#print attributes of the class Dog()
print(f"The breed of the dog is {my_dog.breed}, the name of the dog is {my_dog.name}, and if the dogs has spots: {my_dog.spots}")
print(type(my_dog))

#success