# person.py

import random

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.fun_facts = [
            "I can solve a Rubik's cube in under a minute!",
            "I once met a celebrity at a coffee shop.",
            "I have a collection of over 50 rare stamps.",
            "I know how to juggle five balls at once!"
        ]

    def introduce(self):
        print(f"Hello there! I'm {self.name}. I am {self.age} years old and I identify as {self.gender}.")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"🎉 Happy Birthday, {self.name}! You are now {self.age} years old! 🎉")

    def share_fun_fact(self):
        fact = random.choice(self.fun_facts)
        print(f"Here's a fun fact about me: {fact}")
    
    def update_info(self, name=None, age=None, gender=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if gender:
            self.gender = gender
        print("Updated Information:")
        self.introduce()

# Creating an instance of the Person class
person1 = Person("Alice", 30, "Female")

# Calling methods to showcase functionality
person1.introduce()
person1.celebrate_birthday()
person1.share_fun_fact()
person1.update_info(name="Alicia", age=31, gender="Non-binary")
