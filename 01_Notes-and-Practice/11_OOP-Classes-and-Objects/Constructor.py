class Employee:
    language="Python" # This is a class attribute
    salary=120000

    def __init__(self,name,salary,language): # dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    def getInfo(self):
        
        print(f"The language is {self.language}.The Salary is {self.salary}")

    def greet(self):
        print("Good Morning")
    

pratik = Employee("Pratik",130000,"JavaScript")
print(pratik.name,pratik.salary,pratik.language)
