class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50
student_1 = Student("Anna", [60, 70, 80])
student_2 = Student("Piotr", [30, 40, 45])
print(student_1.is_passed())  # True
print(student_2.is_passed())  # False