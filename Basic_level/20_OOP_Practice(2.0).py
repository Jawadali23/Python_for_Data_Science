"""Level 1: OOP Basics
1️⃣ Class & Object

Create a class Student with:

attributes: name, age

method: display_info() → prints student details"""


# class Student:

#     def __init__(self,name, age):
#         self.name = name 
#         self. age = age

    
#     def display_info(self):
#         print("Name= ",self.name)
#         print("Age= ",self.age)
    
# s1 = Student("Jawad Ali",20)
# s1.display_info()


"""2️⃣ Constructor (__init__)

Create a class Car with:

brand

model

year

Create an object and print all details."""


# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# c1 = Car("Suzuki","VR-52",2020)

# print(c1.brand)
# print(c1.model)
# print(c1.year)

"""3️⃣ Instance vs Class Variable

Create a class Employee:

class variable: company = "Google"

instance variables: name, salary

Create two employees and print their details."""

# class Employee:
#     company = "Google"
    
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary


# e1 = Employee("Ahmed",542000)
# e2= Employee("Ali",50000)
# print(e1.company)
# print(e1.name)
# print(e1.salary)

# print("////////////////")

# print(e2.name)
# print(e2.salary)

"""Level 2: Methods & Encapsulation
4️⃣ Instance Methods

Create a class BankAccount with:

account_holder

balance

Methods:

deposit(amount)

withdraw(amount)

display_balance()"""



# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.balance = balance 

    
#     def deposit(self,amount):
#         # self.amount = amount
#         self.balance +=amount

#     def withdraw(self,amount):
#         # self.amount =amount
#         if amount <= self.balance:
#             self.balance -=amount
#         else:
#             print("Insufficient Balance")

#     def display_balance(self):
#         return self.balance
    
# b = BankAccount("Jawad Ali",2000)
# b.deposit(1000)
# b.withdraw(30000)
# print(b.display_balance())


"""5️⃣ Encapsulation (Private Variables)

Create a class User with:

private variable __password

method check_password(pwd)
"""

# class User:
#     def __init__(self,password):
#         self.__password = password

#     def check_password(self,pwd):
#         if self.__password == pwd:
#             print("Successfully logged in ")
#         else:
#             print("Wrong Password")

# u = User("0000")
# u.check_password("0001")


# class Student:
#     # def __init__(self, name):
#     #     self.__name = name

    
#     def set_name (self,name):
#         self.__name = name
#         if self.__name == "":
#             print("Name can't emply")
#         else:
#             self.__name

#     def get_name (self):
#         return self.__name
    
# s=Student()

# s.set_name("")

# print(s.get_name())


"""6️⃣ Getter & Setter

Create a class Person:

private variable __age

get_age()

set_age(age) (age must be > 0)"""

# class Person:
#     def __init__(self,age):
#         self.__age = age

#     def get_age(self):
#         return self.__age
    

#     def set_age(self,age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age should be in the positive")


# p = Person(10)
# print(p.get_age())
# p.set_age(0)
# print(p.get_age())


"""Level 3: Inheritance
7️⃣ Single Inheritance

Create:

Animal → method sound()

Dog (inherits Animal) → override sound()"""

# class Animal:
#     def sound(self):
#         print("Some Sound")

# class Dog(Animal):

#     def sound(self):
#         print("Bark")


# d = Dog()
# d.sound()


"""8️⃣ super() Keyword

Create:

Vehicle → brand

Bike → brand + mileage
Use super() to initialize parent class."""

class Vehicle:
    def __init__(self,brand):
        self.brand = brand 

class Bike(Vehicle):
    def __init__(self,brand,mileage):
        super().__init__(brand)
        self.mileage = mileage

    def display_info(self):
        print(f"Brand: {self.brand}, Mileage: {self.mileage}")


b = Bike("Honda",2452)
b.display_info()
