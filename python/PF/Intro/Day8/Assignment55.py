#PF-Assgn-55

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number
#Global variable

#ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]
ticket_list = ["AI101:MUM:LON:001", "AI101:MUM:LON:002", "SI456:MUM:SIN:145", "EM456:MUM:DUB:098", "SI456:MUM:SIN:050", "SI456:MUM:SIN:051"] 
def find_passengers_flight(airline_name="AI"):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    count = 0
    for i in ticket_list :
        string_list = i.split(":")
        for j in string_list :
            if j == destination :
                count+= 1
    return count
            
def find_passengers_per_flight():
    list2 = []
    for air in ticket_list :
        list1=air.split(":")
        list2.append(list1[0] + ":" + list1[3])   
    return list2

#         if(re.search(r"[A-Z]{2}\d {3}",air)!=None):
#             print("Match Found: Airlines")
            
def sort_passenger_list():
    temp_list = find_passengers_per_flight()
    temp_list.sort(key=None, reverse=True)
    return temp_list

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())

