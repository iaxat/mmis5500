# Section 10.5
# making data private = encapsulation

import numpy as np

class Person():
    def __init__(self,name,age,height,grades) -> None:
        pass
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades

    def calc_avg_grades(self):
        return np