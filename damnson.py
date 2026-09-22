class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"Name-{self.name}GPA-{self.gpa}"

    @classmethod
    def get_count(cls):
        return f"the total number of students are {cls.count}"

    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa is {cls.total_gpa/cls.count}"


student1 = Student("Spongebob", 7)
student2 = Student("Patrick", 6)
student3 = Student("Rick", 10)
student4 = Student("Morty", 9)
student5 = Student("Jerry", 6)
student6 = Student("Ben10", 6)

print(Student.get_count())
print(Student.get_average())
