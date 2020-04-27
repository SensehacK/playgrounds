'''
Created on Feb 1, 2017

@author: kautilya.save
'''

class Monkey:
    num10 = 10
    print("hello Sensehack")
    
    def add(self,num1 , num2):
        print(num1)
        return num1+ num2
    

first_obj = Monkey()
print(first_obj)
print(first_obj.num10)
print("Memory location of first_obj.num10 before " , id(first_obj.num10))
first_obj.num10=20
print("Memory location of first_obj.num10 after " , id(first_obj.num10))
print(first_obj.num10)
print("Memory location of first_obj.num10 after " , id(first_obj.num10))
print("Memory location first_obj = Monkey() " , id(first_obj))
first_obj.add(10, 23)


third_obj = first_obj
print("Memory location of third_obj = first_obj " , id(third_obj))
third_obj.add(15, 10)
print("Memory location of third_obj.num10 before " , id(third_obj.num10))
print("third_obj.num10",third_obj.num10)
third_obj.num10 = 50
print("third_obj.num10",third_obj.num10)
print("Memory location of third_obj.num10 after " , id(third_obj.num10))


second_obj = Monkey()
second_obj.add(20, 12)
print("Memory location " , id(second_obj))
    
