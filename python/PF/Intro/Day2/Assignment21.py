#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    next_day = day
    next_month = month
    next_year = year
    
    if month in (1 , 3 , 5, 7,8,10) :
        if (day >= 1 and day <=30) :
            next_day = day + 1
        elif (day == 31) :
            next_day = 1
            next_month = month + 1
    
    elif month in ( 4, 6, 9, 11 ) : 
        if (day >= 1 and day <=29) :
            next_day = day + 1
        elif (day == 30) :
            next_day = 1
            next_month = month + 1
  
    elif month == 2 :
        if (day >= 1 and day <=29) :
            next_day = day + 1
        elif (day == 30) :
            next_day = 1
            next_month = month + 1

    elif month == 12 :
        if (day >= 1 and day <=30) :
            next_day = day + 1
        elif (day == 31) :
            next_day = 1
            next_month = 1
            next_year = year + 1
    

    print(next_day,"-",next_month,"-",next_year)

generate_next_date(30,6,2015)
print("Hello 2")
generate_next_date(31,12,2017)