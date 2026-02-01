
"""LEVEL 1 — Very Easy (Basics Warm-up)"""
# 1. Print your name

print("Today,Is my 8th semester result will be announce,I am prayering Allah Almight, and Panjitani pak My result will comes as I work hard This result is all about the four year jounrey hard working and struggle, and I beleive Allah almight give me the good grades.")


# 2. Store age in a variable

age = 21
print("My age is: ", age)


# 3. Add two numbers

num1 =10
num2 =12
result = num1 + num2

print("Sum of two numbers is: ",result)


"""LEVEL 2 — Type Conversion Practice"""


# # 4. Convert string to int

num = "100"
conv = int(num)
print("String to integer: ",type(conv))


# 5. Convert float to int

num = 5.99
result = int(num)
print("Float to integer: ",result)


# 6. Convert number to string

num = 256
conv = str(num)
print("Number to string: ",type(conv))



"""LEVEL 3 — Conditions Practice"""

# 7. Check if a number is positive


num = 0
if num>0:
    print(num,"is positve Number")
elif num<0:
    print(num, "is negative Number")
else:
    print("Zero")



# 8. Check voting eligibility

age = 18
if age >=18:
    print("Eligible")
else:
    print("Not Eligible")

# 9. Even or Odd

num = 16
result = num%2

if result == 0:
    print("Even Number")
else:
    print("Odd Number")



"""LEVEL 4 — Functions"""

# 10. Define a function greet()

def greet():
    print("Hello Python!")
greet()



# 11. Function add(a,b)
def add(a,b):
    return a+b
print("Sum of two Numbers is: ",add(5,8))


# 12. Function is_even(num)

def is_even(num):
    if num%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

is_even(16)


"""LEVEL 5 — Loops Practice"""

# 13. Print numbers 1 to 10

for x in range(1,11):
    print(x)


# 14. Countdown from 5 to 1

num =5
while num>0:
    print(num)
    num -=1


# 15. Sum of numbers 1–10

total = 0
for x in range(1,11):
    total +=x
print("Sum is: ",total)


"""LEVEL 6 — Real Skill Questions"""
# 16. Reverse a number

num =123
rev = 0

while num>0:
    # Extract last digit % 10
    rem = num % 10  
    rev = rev *10 +rem
    # Remove the last digit
    num //=10

print("Reversed Number is: ", rev)


# 17. Print table of 7

def table(num):
    for x in range(1,11):
      result = num*x
      print(num,"x",x,"= ", result)

table(7)

# 18. Print all even numbers from 1 to 50
def is_Even():
   for x in range (1,51):
      if x%2==0:
         print(x,end=" ")
        
is_Even()
