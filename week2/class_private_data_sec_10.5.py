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


# __ double underscore is used to make data private
# need of data privatization is to prevent errors saving it from hackers is not the reason
# Python interpreter handles calling init function because its private that is why we do not need to call it specifically, it is the first that initializes when the class is called

    def calc_avg_grades(self):
        return np.mean(self.grades)

