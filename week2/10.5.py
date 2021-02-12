# Section 10.5
# MMIS 5500
# Class Private Date
# Simulating Private Attributes

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