
class Employee:
    language="Python" # This is a class attribute
    salary=120000

pratik = Employee()
pratik.language ="JavaScript" # This is a object/Instance attribute
print(pratik.language,pratik.sa.ary)
# Here when print function runs, it prints "JavaScript" because instance attribute is present.
# If instance is absent,it prints class attribute