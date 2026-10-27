class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)


s1 = Student("Aman", 85)
s2 = Student("Riya", 90)

s1.display()
s2.display()