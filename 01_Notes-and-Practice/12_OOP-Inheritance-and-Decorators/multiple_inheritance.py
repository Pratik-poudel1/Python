class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.company} and the salary is {self.language}")

class Coder:
    language="Python"
    def printLanguages(self):
        print(f"Your Language:{self.language}")

class Programmer(Employee,Coder):
    company="Google"
    def showLanguage(self):
        print(f"The name is {self.company} and the salary is {self.language}")

b=Programmer()

b.show()
b.showLanguage()
b.printLanguages()