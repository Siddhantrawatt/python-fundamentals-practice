class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(self.name, self.marks)

student = []

for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    student.append(Student(name, marks))
for s in student:
    s.display()

