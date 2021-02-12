# Getters and Setters
# Section 10.3

import numpy as np

# class
class Person():
    def __init__(self, name, age, height, grades) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
    

    # avg grades
    def cal_avg_grades(self):
        return np.mean(self.grades)
    # Setting getters and setters for this class



    # getters/accessors
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height
    
    def get_grades(self):
        return self.grades

    
    # Setters/manipulators
    def set_name(self,name):
        self.name = name
    
    def set_age(self, age):
        self.age = age

    def set_height(self, height):
        self.height = height

    def set_grades(self, grades):
        self.grades = grades




p1 = Person('andy',39,75,[85,89,93])
# p1 is the object

print(p1)

print('age: ',p1.age)
print('name: ',p1.name)
print('height: ',p1.height)
print('grades: ',p1.grades)
print('avg_grades: ',p1.cal_avg_grades())
# calling function from a object would need parentheses

