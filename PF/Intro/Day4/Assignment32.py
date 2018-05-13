#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
        speciality = ""
        print(patient_medical_speciality_list[1])
        count_P = 0 
        count_E = 0
        count_O = 0
        
        print(patient_medical_speciality_list[0])
        
        for i in range ( 0 , len (patient_medical_speciality_list)) :

            for key , value in medical_speciality.items() :
               if patient_medical_speciality_list[i] == key :
                   
                   print(" if (patient_medical_speciality_list[i] == key) :")
                   print(medical_speciality[key])
                   print("medical_speciality[P]")
                   print(medical_speciality["P"])
                   
                  
                   if patient_medical_speciality_list[i] == "P" :
                       count_P += 1
                   
                   elif patient_medical_speciality_list[i] == "O" :
                       count_O += 1
                   
                   elif patient_medical_speciality_list[i] == "E" :
                       count_E += 1
                       
               print("Counts")
               print(count_P)
               print(count_O)
               print(count_E)
                   
               if (count_P > count_O) :
                
                    if (count_P > count_E) :
                        speciality = medical_speciality["P"]
                        #return medical_speciality["P"]
                    
                        #return count_P
                    else :
                        speciality = medical_speciality["E"]
                        #return medical_speciality["E"]
                        #return count_E
                
               elif (count_O > count_E) :
                   speciality = medical_speciality["O"]
                   #return medical_speciality["O"]
                   #return count_O
                   
        return speciality
    
    
#provide different values in the list and test your program   
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
