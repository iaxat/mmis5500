# 10.2
# Advance Python
# Class and Objects

person_dct = {}
person_dct['name'] = 'andy'
person_dct['age'] = 39
person_dct['height'] = 75
person_dct['grades'] = [85,89,93]

print(person_dct)
# dict

# class
class Person():
    def __init__(self, name, age, height, grades) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
    

p1 = Person('andy',39,75,[85,89,93])

print(p1)