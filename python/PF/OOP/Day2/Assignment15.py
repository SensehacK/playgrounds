#OOP-Assgn-15
#Start writing your code here

class Ticket :
    
    __counter = 0
    
    def __init__ (self,passenger_name,source,destination):
        self.__passenger_name = passenger_name
        self.__ticket_id = None
        self.temp_source = source.lower()
        self.temp_dest = destination.lower()
        self.__source = source
        self.__destination = destination

    def get_passenger_name(self):
        return self.__passenger_name
    
    def get_ticket_id(self):
        return self.__ticket_id

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def validate_source_destination(self):
        if (self.temp_source == "delhi") :
            if (self.temp_dest == "mumbai") or (self.temp_dest == "chennai") or (self.temp_dest == "pune") or (self.temp_dest == "kolkata") :
                return True
        else :
            return False
        
    def generate_ticket(self):
        if self.validate_source_destination() :
            Ticket.__counter += 1
            self.__ticket_id =+ Ticket.__counter
            ticket_strconv = str(Ticket.__counter)
            
            if Ticket.__counter < 10 :
                ticket_strconv = ticket_strconv.zfill(2)
        
            first_source = self.get_source()
            first_dest = self.get_destination()
            self.__ticket_id = first_source[0] + first_dest[0] + ticket_strconv
            
        else : 
            self.__ticket_id = None
        
        self.print_ticket()

    def print_ticket(self):
        print("Ticket ID : ", self.get_ticket_id())
        print("Passenger Name : ", self.get_passenger_name())
        print("Ticket Source : ", self.get_source())
        print("Ticket Destination : ", self.get_destination())


#self,passenger_name,source,destination):        
p = Ticket("Kautilya","Delhi" , "Mumbai")
p.generate_ticket()

p2 = Ticket("Sensehack","Delhi" , "Pune")
p2.generate_ticket()
# p1 = Ticket("sense","green")
# p2 = Ticket("sense","green")
# p3 = Ticket("sense","green")        
        
        
    