class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):

        return f"{self.name} : {self.position}"

    @staticmethod
    def is_validposition(position):
        valid_position = ["Mananger", "Site Inspector",
                          "Engineer", "Owner"]
        return position in valid_position


employee1 = Employee("Kartik", "Owner")

employee2 = Employee("Shivansh", "Engineer")

employee3 = Employee("Yuvraj", "Manager")

employee4 = Employee("Swarnim", "Site Inspector")

employee5 = Employee("Nikhil Bisht", "Scientist")

result = Employee.is_validposition("Scientist")
print(result)
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())
