#OOP-Exer-2
#Start writing your code here

class Employee :
    def __init__(self,name,age,salary):
        self.__name = name
        self.salary = salary
        self.age = age
        self__name1 = None
        print("Name:",name)
        print("Age:",age)
        print("Salary:",salary)
        
jack = Employee("Jack","24","34000")
jill = Employee("Jill","25","30000")

jack._Employee__name1 = "Kautilya"

print(jack._Employee__name1)


#print(jack.__name)
