#PF-Assgn-22
def find_leap_years(given_year):
    
    # Write your logic here
    
    list_of_leap_years = []
    count = 0 
    
    while count < 15 :
        if  (given_year % 400 == 0) or (given_year % 100 != 0 and  given_year % 4 == 0) :
            
            list_of_leap_years.append(given_year)
            count = count + 1
            given_year += 1
            
        else :
            given_year += 1
            
    return list_of_leap_years
        
    
    
    '''
    leap_year_list = []
    if given_year % 400 == 0 and given_year % 100 != 0  :
            print("400 years leap year")
    if given_year % 4 == 0 :
        print("Leap Year")
        end_year_range = given_year + 15*4
        
        for i in range (0,15) :
            
            print(given_year)    
            next_leap_year = given_year + 4
            print(next_leap_year)
            given_year = next_leap_year
            if(next_leap_year < end_year_range) : 
                list_of_leap_years = leap_year_list.append(next_leap_year)
                print("leap_year_list")
                print(leap_year_list)
        
        return leap_year_list
        
        
    else :
        print("It is a normal Year")    
        
        
    
    
    return list_of_leap_years
    '''


list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)