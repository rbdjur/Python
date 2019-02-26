class Dog():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

#iteration method
# for pet_class in [felix, niko]:
#     print("inside the loop for polymorphism")
#     print("type", type(pet_class))
#     print("iterant", pet_class)
#     print("type of pet_class.speak", type(pet_class.speak()))
#     print(pet_class.speak())

#common syntax through a function
def pet_speak(pet):
    print(pet.speak())

print("Hey")
pet_speak(niko)
pet_speak(felix)