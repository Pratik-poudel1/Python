
# Example of Class :
class Employee:
    language="Python" # This is a class attribute
    salary=120000
    def getInfo(self):
        print(f"The language is {self.language}.The Salary is {self.salary}")
    def greet(self):
        print("Good Morning")
    

pratik = Employee()
pratik.language = "JavaScript" # This is an instance attribute
# Employee.getInfo(pratik)
pratik.greet()
pratik.getInfo()
