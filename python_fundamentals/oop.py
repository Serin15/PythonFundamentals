#Python is an object-oriented language, meaning you can define and use classes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

# Create an object from the Person class
person = Person("Alex", 30)
person.greet()
