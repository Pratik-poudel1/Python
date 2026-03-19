class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.company} and the salary is {self.salary}")

# class Programmer:
#     company="Google"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and the salary is {self.language}")

class Programmer(Employee):
    company="Google"
    def showLanguage(self):
        print(f"The name is {self.company} and the salary is {self.salary}")

a=Employee()
b=Programmer()

print(a.company,b.company)