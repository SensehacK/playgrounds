class Monkey:
    __no_of_bananas=40
    num = 1

    def eat_banana(self):
        print("eating banana")
        Monkey.__no_of_bananas-=1
    @staticmethod
    def get_banana_count():
        print("No. of bananas left:  ",Monkey.__no_of_bananas)

gopher=Monkey()
doodoo=Monkey()
gopher.eat_banana()
doodoo.eat_banana()
doodoo.get_banana_count() #change made here
print(Monkey.num)
Monkey.num  = 140

print(Monkey.num)
print(Monkey._Monkey__no_of_bananas)