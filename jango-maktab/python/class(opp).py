class human:
    pass
p1= human()
p2= human()

p1.name= 'amirhossein'
p1.lastname = 'keahany'

p2.name= 'ali'
p2.lastname = 'keahany'

# print(p1.name)
# print(p1.lastname)

# print(p2.name)
# print(p2.lastname)
print(30*'-')

#----------------------------------------------------------

class Human:
    def __init__(self, name, lastname):
        self.Name= name
        self.Lastname= lastname
    def __str__(self):
        return f"name:{self.Name}"+ "\n" + f"last_name:{self.Lastname}"
    
print(Human('amir', 'keahany'))

p1= Human("amir", "keahany")
p2= Human("ali", "keahany")

print(p1.Name)
print(p2.Name)
print(30*'-')

#----------------------------------------------------------

#magic method === __method__
#__init__ , __str__ , __len__ , __repr__
print(2+3)
print((2).__add__(3))
print(30*'-')

#----------------------------------------------------------

#ارت بری
class Human:
    def __init__(self, name, lastname):
        self.Name= name
        self.Lastname= lastname
    def __str__(self):
        return f"name:{self.Name}"+ "\n" + f"last_name:{self.Lastname}"
    def name(self):
        return f"my name is {self.Name}"
    
class people(Human):
    def __len__(self):
        return len(self.Name + self.Lastname) 
    def return_name(self):
        return super().name()
    
p1= people('amir', 'keahany')
print(p1)

print(len(p1))
print(p1.return_name())
print(30*'-')

#----------------------------

class Eployee:
    salary= "3000$"                             #class variable= متغییر کلاس
    def __init__(self, name, lastname):
        self.Name= name                         #instance variable= متغیر نمونه
        self.Lastname= lastname
    def name_and_lastname(self):
        return f"name:{self.Name}, Lastname:{self.Lastname}"

print(Eployee("amirhossein", "keahany").name_and_lastname())
print(f"salary:{Eployee.salary}")

#----------------------------------------------------------
#decorator
def hello():
    return 'amir'

hi= hello
print(hi())
#--------------------------------
def function(fun):
    def wrapper():
        return fun()
    return wrapper()

print(function(hello))
#--------------------------------
def function(fun):
    def wrapper():
        print("active")
        return fun()
    return wrapper

@function
def hello():
    return ("name:amir")

print(hello())

#----------------------------------------------------------
import time

def timer(fun):
    def wrapper():
        start= time.time() #زمان اجرای تابع تا این لحظه
        fun()
        end= time.time() - start
        print(f"took {end} second to execute")
    return wrapper

@timer
def counter():
    total= 0
    for item in range(0,10000000):
        total+= item
    return total

counter()
