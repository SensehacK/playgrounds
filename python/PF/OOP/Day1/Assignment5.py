#OOP-Assgn-5
#Start writing your code here

class Instructor :
    
    def __init__(self) :
        self.__avg_feedback = None
        self.__technology_skill = []
        self.__experience = None
        self.__instructor_name = None
        self.__technology = None
        
    def set_technology_skill(self,technology_skill):
        for i in technology_skill :
            self.__technology_skill.append(i)
        
    def get_technology_skill(self):
        return self.__technology_skill
        
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback = avg_feedback
    
    def get_avg_feedback(self):
        return self.__avg_feedback
        
    def set_experience(self,experience):
        self.__experience = experience
        
    def get_experience(self):
        return self.__experience
    
    def set_instructor_name(self,instructor_name):
        self.__instructor_name = instructor_name
        
    def get_instructor_name(self):
        return self.__instructor_name
        
    def set_technology(self,technology):
        self.__technology = technology
        
    def get_technology(self):
        return self.__technology
    
    def check_eligibility(self):
        if ( ( (self.get_avg_feedback() > 4.5) and (self.get_experience() > 3) ) or ( (self.get_avg_feedback() >= 4) and (self.get_experience() <= 3) ) ) :
            for skill in self.get_technology_skill():
                if skill == self.get_technology() :
                    #print("True")
                    return True
        #print("False")        
        return False
                    
            
    def allocate_course(self,technology):
        self.set_technology(technology)
        if self.check_eligibility() :
            return True
        else :
            return False
        

#Initialize Object & set variables
inst = Instructor()
inst.set_avg_feedback(4.7)
inst.set_experience(4)
inst.set_instructor_name("Kautily Save")
skill_list = ["Coding" , "Development" , "Teaching" , "Presentation"]
inst.set_technology_skill(skill_list)

#Call the Method of allocate Course

print(inst.allocate_course("Development"))
print(inst.check_eligibility())
        
        