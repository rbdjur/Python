class Dog():
    #Class object attributes
    species = 'Mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed="poodle", name = "FEFE", spots = True)

print(f"My dog is named {my_dog.name}.  He is a {my_dog.breed}. Does he have spots, you ask? {my_dog.spots}. Oh by the way he is a {my_dog.species}")