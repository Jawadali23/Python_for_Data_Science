
"""
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    
    def display_info(self):
        print("Name= ",self.name,"\n","Age= ",self.age)
    
        
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject= subject


    
    def display_info(self):
        super().display_info()
        print("Subject= ",self.subject)
        
    
    
    
s1 = Teacher("Ahmed",20,"English")

s1.display_info()
"""

# Polymorphism

"""
class Dog:
    
    @staticmethod
    def sound():
        print("Bark")


class Cat:

    @staticmethod
    def sound():
        print("Meow")

    
c1 = [Dog(),Cat()]

for animal in c1:
    animal.sound()
"""


"""
class BankAccount:

    def __init__(self,__balance):
        self.__balance = __balance

    def deposit(self,amount):
        self.__balance += amount
        

    def withdraw(self,amount):
        self.__balance -= amount


    def get_balance(self):
        return self.__balance
    

b1 = BankAccount(10000)
b1.deposit(1000)
b1.withdraw(500)
print(b1.get_balance())

"""


"""
class Car:
    wheels = 4
    def __init__(self,brand,price):
        self.brand =brand
        self.price = price


c1 = Car("Suzuki",7500000)
# print(c1.wheels)
c2= Car("Suzuki",7500000)
c2.wheels=10
print(c2.wheels, c1.wheels)
"""


"""
class Student:
    school_name = "Mehran UET"

    @classmethod
    def class_method(cls,school_name):
        cls.school_name = school_name


s1= Student()
s1.class_method("Mehran UET, Jamshoro")
print(s1.school_name)
"""


"""
class MathUtils:

    @staticmethod
    def is_even(num):
        return num % 2 ==0
    

m =MathUtils()

print(m.is_even(10))
print(m.is_even(11))
"""

# class Test:
#     x =10

# t1 =Test()
# t2 =Test()

# t1.x =99

# print(t2.x)



"""
class Student:
    school_name = "Mehran UET"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)
    
    def grade(self):
        avg = self.average_marks()
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "fail"
        
    
s1 = Student("Ali", [85,60,85])
s2= Student("Sara",[85,69,95])

print(s1.school_name)
print(s1.name, "Average= ",s1.average_marks(),"Grade= ",s1.grade())
print(s2.name, "Average= ",s2.average_marks(),"Grade= ",s2.grade())

"""

"""
class Book:

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Price: ",self.price)

c1 = Book("Story of Success","Ahmed khan",450)
c1.display()
"""


"""
class Laptop:
    def __init__(self,brand,ram,price=50000):
        self.brand = brand
        self.ram = ram
        self.price = price


    def display(self):
        print("Brand: ",self.brand)
        print("Ram: ",self.ram)
        print("Price: ",self.price)

c1 = Laptop("HP","8 GB")
c2 = Laptop("Dwell"," 16 GB",450000)
c1.display()
c2.display()
"""

"""
class Employee:

    __salary = 0

    def set_salary (self,value):
        if value > 30000: 
            self.__salary = value
        return self.__salary
    
    def get_salary(self):
        return self.__salary
    

e1 =Employee()
print(e1.set_salary(5585))
print(e1.get_salary())

"""

"""

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand= ",self.brand)
        print("Model= ",self.model)
        # print("Seats= ",self.seats)

    
class Car(Vehicle):
    def __init__(self,brand,model,seats):
        self.brand = brand
        self.model= model
        self.seats= seats
    
    def display(self):
        super().display()
        print("Seats= ",self.seats)
    
cr1 =Vehicle("Suzuki","VR-754")
cr1.display()
cr1 = Car("Hondu","civic",6)
cr1.display()
"""



"""
class Dog:

    @staticmethod
    def sound():
        print("Bark")

class Cat:

    @staticmethod
    def sound():
        print("Meow")


class Cow:
    
    @staticmethod
    def sound():
        print("Moo")


animal = [Dog(),Cat(),Cow()]

for val in animal:
    val.sound()

"""



"""
class School:

    name = "ABC School"

    @classmethod
    def change_name(cls,name):
        cls.name = name 


    @staticmethod
    def is_valid_student(age):
        return age >=5
    

s1 = School()

s1.change_name("Mehran UET")

print(s1.is_valid_student(5))



class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age


class Employee:
    def __init__(self,salary):
        self.salary= salary


class Manager(Person,Employee):
    def __init__(self, name,age,salary):
        Person.__init__(self,name,age)
        Employee.__init__(self,salary)

    def display(self):
        print("Name= ",self.name)
        print("Age= ",self.age)
        print("Salary= ",self.salary)

m = Manager("Ali",22,50000)
m.display()

"""



"""
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def set_salary(self):
        if self.salary < 20000:
            return self.salary
        
e1=Employee("Ali",10000)
print(e1.set_salary())

"""

"""
class Account:
    def __init__(self,__pin):
        self.__pin = __pin

    def set_pin(self):
        return self.__pin

        
    
    def check_pin(self):
        if int(self.__pin) == 4:
            return self.__pin
        

a = Account(1234)
a.set_pin(1024)
print(a.check_pin(1025))
"""

