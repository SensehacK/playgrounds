#OOP-Assgn-9
#Implement Student class here


class Student :
    
    def __init__(self) :
        self.__student_id = None
        self.__marks = None 
        self.__age = None
        self.__fees = None
        self.__course_id = None
        self.__student_gender = None


    def validate_marks(self):
        if ((self.get_marks() >= 0) and (self.get_marks() <= 100)) :
            return True
        else :
            return False
        
    def validate_age(self):
        if self.get_age() > 20 :
            return True
        else :
            return False

    def check_qualification (self):
        if (self.validate_age() and self.validate_marks() and  self.get_marks() >= 65) :
            return True
        else :
            return False
        
    def choose_course(self,course_id):
        
        if (course_id == 1001) :
            self.set_course_id(course_id)
            if self.get_marks() > 85 :
                discount = (25575.0 - (25575.0 * (25/100)))
                self.set_fees(discount)
            else : 
                self.set_fees(25575.0)
            return True
        
        elif (course_id == 1002):
            self.set_course_id(course_id)
            if self.get_marks() > 85 : 
                discount2 = (15500.0 - (15500.0 * (25/100)))
                self.set_fees(discount2)
            else :
                self.set_fees(15500.0)
            return True

        else :
            return False
        
    def get_student_id(self):
        return self.__student_id
    
    def set_student_id(self,student_id):
        self.__student_id = student_id
    
    def set_marks(self,marks):
        self.__marks = marks
    
    def get_marks(self):
        return self.__marks

    def set_age(self,age):
        self.__age = age
    
    def get_age(self):
        return self.__age

    def set_course_id(self,course):
        self.course_id = course
    
    def get_course_id(self):
        return self.__course_id
    
    def set_fees(self,fees):
        self.__fees = fees
    
    def get__fees(self):
        return self.__fees
    
    
maddy=Student() 
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id") 
else:
    print("Student has not qualified")

# #Initialize Object & set variables
# stud = Student()
# stud.set_student_id(1001)
# stud.set_age(25)
# stud.set_marks(105000)
# stud.validate_age()
# stud.validate_marks()
# stud.check_qualification()
#         


































