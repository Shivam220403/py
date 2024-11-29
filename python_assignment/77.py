class Animal:
    pass

class Dog(Animal):
    pass

animal = Animal()
dog = Dog()

print("Using type():")
print(type(animal) == Animal)
print(type(dog) == Dog)
print(type(dog) == Animal)

print("\nUsing isinstance():")
print(isinstance(animal, Animal))
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
