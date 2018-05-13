'''
Created on Feb 15, 2017

@author: kautilya.save
'''
class Alpha :
    
    def one(self):
        return 10
    def two(self):
        return self.one()
    
    
class Beta(Alpha):
    def one(self):
        return 10
    def three(self):
        return 10     
    
class Gamma(Beta):
    def one(self):
        return 10
    def three(self):
        return super().two()     
    def four(self):
        return self.one()
    def five(self):
        return 10     
    
    
go = Gamma()


num1 = go.two() + go.three() + go.four()

num2 =  go.three() + go.four() + go.one()

num3 =  go.one() +go.two() + go.three() 







