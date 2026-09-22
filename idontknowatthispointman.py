class Student():
    passing_year = 2027
    numberof_students = 0

    def __init__(self, name, age, stream):
        self.name = name
        self.age = age
        self.stream = stream
        Student.numberof_students += 1


student1 = Student("Rick", 70, "Science")
student2 = Student("Morty", 14, "Mathematics")
student3 = Student("Jerry", 40, "Social Studies")
print(
    f"My class of Graduation year {Student.passing_year} has {Student.numberof_students}")
print(student1.name)
print(student2.name)
print(student3.name)
