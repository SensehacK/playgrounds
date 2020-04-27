#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    p_count = 0
    e_count = 0
    o_count = 0
    for i in patient_medical_speciality_list:
        if i == "P":
            p_count = p_count + 1
        elif i == "E":
            e_count = e_count + 1
        elif i == "O":
            o_count = o_count + 1
    if p_count > e_count:
        if p_count > o_count:
            max = "P"
        else:
            max = "O"
    else:
        if e_count > o_count:
            max = "E"
        else:
            max = "O"
    
    for key,value in medical_speciality.items():
        if key==max:
            speciality = value
        
    return speciality
    
#provide different values in the list and test your program   
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)