# Section 10.5
# making data private = encapsulation

import numpy as np


class Person():

# __init__ is a constructor also known as initializer
    def __init__(self,name,age,height,grades,address) -> None:
        pass
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
        self.__address = address
# __ dpuble uncderscore is used to make data private


    def calc_avg_grades(self):
        return np.mean(self.grades)

