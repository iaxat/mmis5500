# Section 10.5
# MMIS 5500
# Class Private Date
# Simulating Private Attributes
# With private data, getter and setter is a necessity


class Person():
    def __init__(self, name, age, height, grades, ssn) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.grades = grades
        self.__ssn = ssn

    # avg grades
    def cal_avg_grades(self):
        return np.mean(self.grades)
    # Setting getters and setters for this class


    # getter and setter for private data ssn
    def get_ssn(self):
        return self.__ssn

    def set_ssn(self, ssn):
        self.__ssn = ssn

    

# applying
p1 = Person('andy', 39, 75, [89,93,87], 11111111)

print(p1.get_ssn())
p1.set_ssn(999999999)
print(p1.get_ssn())
