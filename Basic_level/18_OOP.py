
"""
class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
            avge=sum/3
        return avge
    

    @staticmethod
    def hello():
        print("Hello")

s1 = Student("ABCD",[78,85,95])
print("Hi",s1.name,"your score is: ",s1.avg())
s1.hello()

s1.name ="XYZ"
print("Hi",s1.name,"your score is: ",s1.avg())
"""
"""
class Account:
    def __init__(self,bal,acc_no):
        self.balance = bal
        self.account_no = acc_no


    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount,"was debited")
        print("Total balance =",self.get_balance())

    
    def credit(self,amount):
        self.balance +=amount
        print("Rs.",amount,"was credited")
        print("Total balance =",self.get_balance())


    def get_balance(self):
        return self.balance
    

acc1 =Account(10000,12345)

acc1.debit(500)
acc1.credit(1000)

"""

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

    # def display(self):
    #     print(self.name)
    #     print(self.marks)

#     def is_pass(self):
#         if self.marks >= 40:
#             print("Pass")
#         else:
#             print("Fail")



# s1= Student("Ahmed",32)

# s1.is_pass()

"""
class Employee:
    company ="Google"

    def __init__(self,name,salary):
        self.name =name
        self.salary = salary
    
    def show_details(self):
        print("Employee name is ",self.name,"It's salary is ",self.salary)

    
e1 =Employee("ABCD",40000)
print("Company name ",Employee.company)
e1.show_details()

e2 =Employee("Ahmed",50000)
print("Company name ",Employee.company)
e2.show_details()
    """

"""
class BankAccount:
    _balance = 10000

    def deposit(self, amount):
        self._balance +=amount
        return amount
    
    def withdraw(self, amount):
        self._balance -= amount
        return amount

    def get_balance(self):
        return self._balance
    

b1= BankAccount()
print(b1.deposit(1000))
print(b1.get_balance())
print(b1.withdraw(500))
print(b1.get_balance())

"""



# Private Attribute & Methords

"""
class Account:
    acc_no = "1234"
    __acc_pass ="ABCD"

    def get_pass(self):
        print(self.__acc_pass)

acc1 = Account()
print(acc1.acc_no)
print(acc1.get_pass())

"""

"""
class Person:
    __name = "anouymous"

    def __hello(self):
        print(self.__name)
    

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())

"""


# Inheritance
# Single and multi-level Inheritance 

"""

class Car:

    @staticmethod
    def start():
        print("Start the car..")

    @staticmethod
    def stop():
        print("Stop the car..")


class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand


class Furtuner(ToyotaCar):
    def __init__(self,model):
        self.model= model



car1 = Furtuner ("VR_452")
print(car1.color)
"""
# car1 = ToyotaCar("Furtune")
# car2 = ToyotaCar("Suzuki")

# print(car1.name)
# car1.start()

# car2.stop()

# print(car2.color)



# Multiply Inheritance


# class A:
#     a ="Hello"

# class B:
#     b = "Who are you?"

# class C(A,B):
#     c = "Where are you from?"


# cl = C()

# print(cl.a,"",cl.b,"",cl.c)



# Super () Method

"""
class Car:
    def __init__(self, color):
        self.color = color

    @staticmethod
    def start():
        print("Start the Car..")

    @staticmethod
    def stop():
        print("Stop the Car..")


class ToyotaCar(Car):

    def __init__(self,color,model):
        super().__init__(color)
        self.model = model


car1 = ToyotaCar("Blue","VR-4512")
print(car1.color)
car1.start()
"""

# @classmethod
"""
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name
    

p1= Person()
p1.changeName("Ahmed")
print(p1.name)

"""
# @property

"""

class Subject:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3)+ "%"
    

sub = Subject(95,98,85)
print(sub.percentage)

sub.phy = 50
print(sub.percentage)
"""


# Polymorphizim


"""
class Complex:
    def __init__(self,real, img):
        self.real =real 
        self.img =img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg) 
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

    
num1 = Complex(1,5)
num1.showNumber()

num2 =Complex(2,8)
num2.showNumber()


num3 =num1 + num2
num3.showNumber()

num3 = num1-num2
num3.showNumber()


"""

"""
class Circle:
    def __init__(self,radius):
        self.radius = radius

    
    def area(self):
        return (22/7) * self.radius **2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

"""

"""
class Employee:
    def __init__(self,role,depart,salary):
        self.role = role
        self.depart = depart
        self.salary = salary

    def showDetail(self):
        print("Name= ",self.name)
        print("Age= ",self.age)
        print("Roll= ",self.role)
        print("Department= ",self.depart)
        print("Salary= ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        super().__init__("Engineer","IT","80,000")

# e1= Employee("Accountant","Finance",60000)
e1= Engineer("Elon Musk",40)
e1.showDetail()
"""


"""
class Order:
    def __init__(self,item,price):
        self.item = item 
        self.price = price 

    
    def __gt__(self,num2):
        return self.price > num2.price
    
or1 = Order("Chips", 30)
or2 = Order("Tea", 40)
print(or1 > or2)
"""