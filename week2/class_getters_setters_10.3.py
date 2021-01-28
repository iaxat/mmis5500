# Section 10.3

import numpy as np


person_dict = {}
person_dict['name'] = 'axat'
person_dict['age'] = 25
person_dict['height'] = 59
person_dict['grades'] = [98, 96, 102]

print(person_dict)


class Person():
    def __init__(self, name, age, height, grades) -> None:
        pass
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades

    def calc_avg_grades(self):
        return np.mean(p1.grades)

# getter and setter functions to manipulate the values
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height
    
    def get_grades(self):
        return self.grades
    

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def set_height(self,height):
        self.height = height

    def set_grades(self, grades):
        self.grades = grades



p1 = Person('axat', 25, 59, [98, 96, 102])
print(p1)
print('')
print(p1.age)
print(p1.grades)
print(p1.name)

print(p1.calc_avg_grades())
