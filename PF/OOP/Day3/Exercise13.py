#OOP-Exer-13
class Juggler:
    def __init__(self,name):
        self.__name=name
    
    def juggles(self,obj1):
        print(self.__name , "is juggling with " , obj1.get_name())
        

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
        
ga = Juggler("Kautilya")
gugg = JugglingItem("Knives")
ga.juggles(gugg)




ga1 = Juggler("Suresh")
gugg1 = JugglingItem("Balls")
ga1.juggles(gugg1)

