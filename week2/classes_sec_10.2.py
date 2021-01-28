# From the course MIS 5500
# Advance Python
# By Andrew Brim

# Section 10.2 
# Classes and Objects
# Book: Intro to Computer Science

# This program covers difference between Dict and Classes

from typing import AsyncGenerator


person_dict = {}
person_dict['name'] = 'axat'
person_dict['age'] = 25
person_dict['height'] = 59
person_dict['grades'] = [98,96,102]

print(person_dict)

class Person():
    def __init__(self,name,age,height,grades) -> None:
        pass
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades

p1 = Person('axat',25,59,[98,96,102])
print(p1)
print('')
print(p1.age)
print(p1.grades)
print(p1.name)

