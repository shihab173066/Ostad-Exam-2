import json

class Person:
    def __init__(self, name, age, address):
        self.name = name               # Initialize name of the person
        self.age = age                 # Initialize age of the person
        self.address = address         # Initialize address of the person

    def display_person_info(self):
        # Display the person's information
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")
