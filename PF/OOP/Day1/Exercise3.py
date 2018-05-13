#OOP-Exer-3
#Start writing your code here

class Employee :
    def __init__(self,name,age,salary):
        self.name = name
        self.salary = salary
        self.age = age
        print("Name:",name)
        print("Age:",age)
        print("Salary:",salary)
        
Tom = Employee("Tom","24","45000")
