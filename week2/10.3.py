# Getters and Setters
# Section 10.3
# MMIS 5500
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

p1 = Person('andy',39,75,[85,89,93])
# p1 is the object

print(p1)

print('age: ',p1.age)
print('name: ',p1.name)
print('height: ',p1.height)
print('grades: ',p1.grades)
print('avg_grades: ',p1.cal_avg_grades())
# calling function from a object would need parentheses