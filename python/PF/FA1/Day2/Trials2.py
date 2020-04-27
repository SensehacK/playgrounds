'''
what is the output of the following program?

def fun(x,y):
    try:
        if(x[0]//y==0):
            print(1)
        else:
            print(2)
        print(3)
    except:
        print("Some other error occurred")
    except ValueError:
        print(4)
    except IndexError:
        print(5)
    except TypeError:
        print(10)
    except ZeroDivisionError:
        print(6)
    finally:
        print(7)
    print(8)
fun("1234",0)
print(9)









what is the output of the following program?


def fun(x,y):
    try:
        a=int(x)
        if(a//y==0):
            print(1)
        else:
            print(2)
        print(3)
    except ValueError:
        print(4)
    except IndexError:
        print(5)
    except ZeroDivisionError:
        print(6)
    finally:
        print(7)
    print(8)

fun("A",0)
print(9)




what is the output of the following program?
'''
import re




'''
input1="Savana Airlines E101"
print(re.sub(r"E(\d{3})",r"#\1",input1))


what is the output of the following program?


input1="Savana Airlines E101"
print(re.sub(r"E(\d{3})",r"#\1",input1))




def fun(x,y):
    try:
        z=x+y
        print(z)
    except ValueError:
        print(0)
    print(9)
try:
    fun(2,'2')
    print(1)
except TypeError:
    print(3)
except NameError:
    print(4)
except ValueError:
    print(5)
finally:
    print(6)
print(7)
'''

#==============================
def fun(x,y):
    try:
        z=x+y
        print(z)
    except ValueError:
        print(0)
    print(9)
try:
    fun(2,None)
    print(1)
    
# except Exception:
#     print(2)
except TypeError:
    print(3)
except NameError:
    print(4)
except ValueError:
    print(5)
finally:
    print(6)
print(7)



'''
===============================
def fun(x,y):
    try:
        z=x+y
        print(z)
    except TypeError:
        print(0)
    print(9)
try:
    fun(2,'2')
    print(1)
except Exception:
    print(2)
except TypeError:
    print(3)
except NameError:
    print(4)
except ValueError:
    print(5)
finally:
    print(6)
print(7)
==============================

def fun(x):
    if(x=="qwe"):
        return x
    else:
        x=x[:-1]
        return fun(x)


str1="qwerty"
str2=fun(str1)
print(str1,str2)
==========================
def fun(x):
    if(x=="qwe"+x):
        return x
    else:
        x=x[:-1]
        return fun(x)


str1="qwerty"
str2=fun(str1)
print(str1,str2)
=====================
def fun(x):
    if(x=="qwe"+x):
        return x
    else:
        x="qwe"+x[:-1]
        return fun(x)


str1="qwerty"
str2=fun(str1)
print(str1,str2)
======================
def fun(x,y):
    if(len(x)==2):
        return x
    else:
        x.pop()
        y.append(fun(x,y)+[0])
        

list1=[1,2,3,4,5]
list2=[]
fun(list1,list2)
print(list1,list2)
====================
from src.resources.DataStructures import Stack

def fun(x):
    s1=Stack(x.max_size)
    x.pop()
    while(not x.is_empty()):
        s1.push(x.pop()+1)
    return s1
stack1=Stack(5)
stack1.push(1)
stack1.push(5)
stack1.push(7)
stack1.push(2)
stack1.push(9)
fun(stack1).display()
==================
from src.resources.DataStructures import Stack

def fun(x):
    s1=Stack(x.max_size)
    y=x.pop()+x.pop()
    x.push(y)
    while(not x.is_empty()):
        s1.push(x.pop()+1)
        x.push(s1.pop())
        x.pop()
    return s1
stack1=Stack(5)
stack1.push(1)
stack1.push(5)
stack1.push(7)
stack1.push(2)
stack1.push(9)
fun(stack1).display()
==================================
from src.resources.DataStructures import Stack

def fun(x):
    s1=Stack(x.max_size)
    y=x.pop()+x.pop()
    x.push(y)
    while(not x.is_empty()):
        s1.push(x.pop()+1)
        x.push(s1.pop())
        x.pop()
    return x
stack1=Stack(5)
stack1.push(1)
stack1.push(5)
stack1.push(7)
stack1.push(2)
stack1.push(9)
fun(stack1).display()
========================================


from src.resources.DataStructures import Stack

def fun(x):
    s1=Stack(x.max_size)
    y=x.pop()+x.pop()
    x.push(y)
    while(not x.is_empty()):
        s1.push(x.pop()+1)
        x.push(2)
        x.pop()
    return s1
stack1=Stack(5)
stack1.push(1)
stack1.push(5)
stack1.push(7)
stack1.push(2)
stack1.push(9)
fun(stack1).display()
===================================
from src.resources.DataStructures import Stack

def fun(x):
    s1=Stack(x.max_size)
    y=x.pop()+x.pop()
    x.push(y)
    while(not x.is_empty()):
        s1.push(x.pop()+1)
        s1.push(2)
        x.pop()
    return s1
stack1=Stack(5)
stack1.push(1)
stack1.push(5)
stack1.push(7)
stack1.push(2)
stack1.push(9)
fun(stack1).display()
===============================
from src.resources.DataStructures import Stack

def fun(x):
    s1=Stack(x.max_size)
    y=x.pop()
    x.push(y+3)
    while(x.pop() != 5):
        s1.push(x.pop()+1)
        s1.push(2)
        x.pop()
    return s1
stack1=Stack(5)
stack1.push(1)
stack1.push(5)
stack1.push(7)
stack1.push(2)
stack1.push(9)
fun(stack1).display()
===============================

from src.resources.DataStructures import LinkedList
 
def fun(x):
    temp=x.next
    for item in [1,2,3]:
        while (temp.next!=None):
            if(temp.data==item):
                temp.data+=item
            else:
                temp.data=temp.next.data
            temp=temp.next
                
    

l1=LinkedList()
l1.add(4)
l1.add(7)
l1.add(3)
l1.add(1)
l1.add(8)

fun(l1.head)
l1.display()
=======================

from src.resources.DataStructures import LinkedList
 
def fun(x):
    #temp=x.next
    for item in [1,2,3]:
        temp=x.next
        while (temp.next!=None):
            if(temp.data==item):
                temp.data+=item
            else:
                temp.data=temp.next.data
            temp=temp.next
                
    

l1=LinkedList()
l1.add(4)
l1.add(7)
l1.add(3)
l1.add(1)
l1.add(8)

fun(l1.head)
l1.display()
=============================

from src.resources.DataStructures import LinkedList
 
def fun(x):
    temp=x.next
    if(temp==None):
        return
    while (temp.next!=None):
        if(temp.data in [1,3]):
                temp.data+=1
                fun(x)
                
        temp=temp.next
                
    

l1=LinkedList()
l1.add(4)
l1.add(7)
l1.add(3)
l1.add(1)
l1.add(8)

fun(l1.head)
l1.display()
===============================


from src.resources.DataStructures import LinkedList
 
def fun(x):
    temp=x.next
    if(temp==None):
        return
    while (temp.next!=None):
        if(temp.data in [1,3]):
                temp.data+=1
                fun(x)
                print(temp.data)
        temp=temp.next
                
    

l1=LinkedList()
l1.add(4)
l1.add(7)
l1.add(3)
l1.add(1)
l1.add(8)

fun(l1.head)
l1.display()
===============================
class A:
    def __init__(self,x):
        self.__x=x

    def get_x(self):
        return self.__x


    def set_x(self, value):
        self.__x = value

class B(A):
    def __init__(self,y):
        super().__init__(y+1)
        self.__y=y

    def get_y(self):
        return self.__y
b=B(5)
print(b.get_x())
        
=========================
class A:
    def __init__(self,x):
        self.__x=x

    def get_x(self):
        return self.__x


    def set_x(self, value):
        self.__x = value

class B(A):
    def __init__(self,y):
        self.set_x(y+1)
        self.__y=y
    


    def get_y(self):
        return self.__y
b=B(5)
print(b.get_x())
        
==============================
class A:
    def __init__(self,x):
        self.__x=x

    def get_x(self):
        return self.__x


    def set_x(self, x):
        self.__x = x

class B(A):
    def __init__(self,y):
        
        self.__y=y
        print(self.get_x())
        super().__init__(y+1)
    


    def get_y(self):
        return self.__y
b=B(5)
print(b.get_x())
 ================================
  from abc import abstractmethod
class A:
    def __init__(self,x):
        self.__x=x

    def get_x(self):
        return self.__x


    def set_x(self, x):
        self.__x = x
    @abstractmethod
    def A(self):
        pass

class B(A):
    def __init__(self,y):
        
        self.__y=y
        print(self.get_x())
        super().__init__(y+1)
    


    def get_y(self):
        return self.__y
b=B(5)
print(b.get_x())
        
===============================
from abc import ABCMeta,abstractmethod
class A(metaclass=ABCMeta):
    def __init__(self,x):
        self.__x=x

    def get_x(self):
        return self.__x


    def set_x(self, x):
        self.__x = x
    @abstractmethod
    def A(self):
        pass

class B(A):
    def __init__(self,y):
        
        self.__y=y
        
        super().__init__(y+1)
    


    def get_y(self):
        return self.__y
class C(B):
    def A(self):
        print(1)
b=C(5)
print(b.get_x())
=============================
from abc import ABCMeta,abstractmethod
class A(metaclass=ABCMeta):
    def __init__(self,x):
        self.__x=x

    def get_x(self):
        return self.__x


    def set_x(self, x):
        self.__x = x
    @abstractmethod
    def A(self):
        pass

class B(A):
    def __init__(self,y):
        
        self.__y=y
        
        super().__init__(y+1)
    


    def get_y(self):
        return self.__y
class C(B):
    def A(self):
        print(1)
b=B(5)
print(b.get_x())
==================================
from abc import ABCMeta,abstractmethod
class A(metaclass=ABCMeta):
    def __init__(self,x):
        self.__x=x

    def get_x(self):
        return self.__x


    def set_x(self, x):
        self.__x = x
    @abstractmethod
    def A(self):
        pass

class B(A):
    def __init__(self,y):
        
        self.__y=y
        
        super().__init__(y+1)
    


    def get_y(self):
        return self.__y
class C(B):
    def A(self):
        self.__x=5
b=C(3)
print(b.get_x())
====================================
from abc import ABCMeta,abstractmethod
class A(metaclass=ABCMeta):
    counter=1001
    def __init__(self,x):
        self.__x=x
        self.counter+=1

    def get_x(self):
        return self.__x


    def set_x(self, x):
        self.__x = x
    @abstractmethod
    def A(self):
        pass

class B(A):
    def __init__(self,y):
        
        self.__y=y
        
        super().__init__(y+1)
        A.counter+=1
    


    def get_y(self):
        return self.__y
class C(B):
    def A(self):
        self.__x=5
        A.counter+=1
b=C(3)
b.A()
print(A.counter)     
====================================
from abc import ABCMeta,abstractmethod
class A(metaclass=ABCMeta):
    counter=1001
    def __init__(self,x):
        self.__x=x
        A.counter+=1

    def get_x(self):
        return self.__x


    def set_x(self, x):
        self.__x = x
    @abstractmethod
    def A(self):
        pass

class B(A):
    def __init__(self,y):
        
        self.__y=y
        
        super().__init__(y+1)
        A.counter+=1
    


    def get_y(self):
        return self.__y
class C(B):
    def A(self):
        self.__x=5
        A.counter+=1
b=C(3)
b.A()
print(A.counter)     
==========================================
X={"x":3,"y":2,"z":7,"a":6}

def fun(t):
    for key,value in X.items():
        if(key==t):
            return value
    return -1
print(fun("y"))
====================================
X={"x":3,"y":2,"z":7,"a":6}

def fun(t):
    if(t in X.keys()):
        return X[t]
    
    return -1
print(fun("y"))
=========================================
#find no of astricks that get printed#

x=4
y=3
while(y!=0):
    while(x!=0):
        if(x>=1):
            continue
            print("*")
        x-=1
        print("*")
    if(y<=x):
        break
    print("*")
    y-=1
''''it will give infinite loop'''
    
'''
==========================================
x=4
y=3
while(y!=0):
    while(x!=0):
        if(x>=1):
            x-=1
            continue
            print("*")
        print("*")
    if(y<=x):
        break
    print("*")
    y-=1
======================================
'''
