#OOP-Assgn-32
#Start writing your code here
from abc import ABCMeta, abstractmethod

class Employee(metaclass = ABCMeta) :
    
    def __init__(self,job_band,employee_name , basic_salary , qualification):
        self.__job_band = job_band
        self.__employee_name = employee_name
        self.__basic_salary = basic_salary
        self.__qualification = qualification
        
    def get_job_band(self):
        return self.__job_band

    def get_employee_name(self):
        return self.__employee_name

    def get_basic_salary(self):
        return self.__basic_salary

    def get_qualification(self):
        return self.__qualification

    @abstractmethod
    def validate_job_band(self):
        pass
    
    @abstractmethod
    def calculate_gross_salary(self):
        pass
    
    def validate_basic_salary(self):
        if self.get_basic_salary() > 3000 : 
            return True
        return False
    
    def validate_qualification(self):
        if self.get_qualification() == "Bachelors" or self.get_qualification() == "Masters" :
            return True
        return False
        
class Lateral (Employee) :
    
    def __init__(self,job_band,employee_name , basic_salary , qualification,skill_set): 
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__skill_set = skill_set

    def get_skill_set(self):
        return self.__skill_set
    
    def validate_job_band(self):

        x =  self.get_job_band()
        if x in ("D", "E" ,"F"):
            print('found x')
            return True
        else :
            return False
    
    def calculate_gross_salary(self):
        gross_salary = 0
        basic_salary = self.get_basic_salary()
        pf_amount  = basic_salary * 12 / 100
        skill = self.get_skill_set()
        job_band = self.get_job_band()
        incentive = 0
        sme_bonus = 0
        
        if skill == "AGP":
            sme_bonus = 6500
        elif skill == "AGPT":
            sme_bonus = 8200
        elif skill == "AGDEV":
            sme_bonus = 11500    
        else :
            sme_bonus = 0
            print("Improper SKILL sme_bonus")
        
        if job_band == "D" :
            incentive = basic_salary * 13 / 100
        elif job_band == "E" :
            incentive = basic_salary * 16 / 100
        elif job_band == "F" :
            incentive = basic_salary * 20 / 100
        else :
            incentive = 0
            print("Improper incentive job_band")
        
        if self.validate_basic_salary() and self.validate_job_band() and self.validate_qualification() :
            gross_salary = basic_salary + pf_amount + sme_bonus + incentive   
            return gross_salary     
        else :
            gross_salary = -1
            return gross_salary
        
class Graduate (Employee) :
    
    def __init__(self,job_band,employee_name , basic_salary , qualification,cgpa): 
        super().__init__(job_band, employee_name, basic_salary, qualification)
        self.__cgpa = cgpa

    def get_cgpa(self):
        return self.__cgpa

    def validate_job_band(self):
        x =  self.get_job_band()
        
        if x in ("A", "B" ,"C"):
            print('found x')
            return True
        else :
            return False
        
    def calculate_gross_salary(self):
        gross_salary = 0
        basic_salary = self.get_basic_salary()
        pf_amount  = basic_salary * 12 / 100
        cgpa = self.get_cgpa()
        job_band = self.get_job_band()
        incentive = 0
        tpi_amount = 0
        
        if cgpa >= 4 and cgpa <= 4.25 :
            tpi_amount = 1000
        elif cgpa >= 4.26 and cgpa <= 4.5 :
            tpi_amount = 1700
        elif cgpa >= 4.51 and cgpa <= 4.75 :
            tpi_amount = 3200
        elif cgpa >= 4.76 and cgpa <=5 :
            tpi_amount = 5000
        else :
            tpi_amount = 0
            print("Improper CGPA")
        
        if job_band == "A" :
            incentive = basic_salary * 4 / 100
        elif job_band == "B" :
            incentive = basic_salary * 6 / 100
        elif job_band == "C" :
            incentive = basic_salary * 10 / 100
        else :
            incentive = 0
            print("Improper incentive job_band")
        
        if self.validate_basic_salary() and self.validate_job_band() and self.validate_qualification() :
            gross_salary = basic_salary + pf_amount + tpi_amount + incentive 
            return gross_salary   
        else :
            gross_salary = -1
            return gross_salary
        
    
lat = Lateral("E","Kautilya" , 4000 , "Masters","AGP")
grad = Graduate("A","Kautisalya" , 5000 , "Masters",4.76)
lat.calculate_gross_salary()

grad.calculate_gross_salary()
