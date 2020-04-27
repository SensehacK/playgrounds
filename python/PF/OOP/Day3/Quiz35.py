'''
Created on Feb 3, 2017

@author: kautilya.save
'''
class A:
    def m1(self):
        return 20
class B(A):
    def m1(self):
        print("Hello m1 b")
        val=super().m1()+30
        return val
class C(B):
    def m1(self):
        print("Hello m1 c")
        val=self.m1()+20
        return val
obj=C()
print(obj.m1())