# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(self.name, "makes a sound")


# Child class
class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)   # Call parent constructor
        self.breed = breed

    # Override parent method
    def make_sound(self):
        print(self.name, "says Woof!")

    # New method for Dog
    def show_breed(self):
        print("Breed:", self.breed)


# Create object
dog = Dog("Buddy", "Labrador")

dog.make_sound()       # Overridden method
dog.show_breed()       # Child's own method

# Check whether Dog is a subclass of Animal
print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))