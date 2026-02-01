"""LEVEL A — Logic Warm-Up"""

# 1️⃣ Check the largest of two numbers

"""
a=12
b=9
if a > b:
    print(a,"is greater ") 

elif b > a:
    print(b,"is greater ")
else:
    print("Both number are equal")

"""
# 2️⃣ Check if a number is divisible by both 3 and 5 

"""
num = int(input("Enter you number: "))

if num%3 == 0 and num %5 ==0:
    print(num,"-> Yes")
else:
    print(num, "-> No")

    """

# 3️⃣ Find the square only if number is even

"""
num = int(input("Enter you number: "))

if num%2==0:
    print(num,"->",num**2)
else:
    print(num,"-> Not Allowed")

    """

# 4️⃣ Print numbers from 1 to 20
# Skip multiples of 3

"""
for x in range(1,21):
    if x % 3 == 0:
        continue
    print(x,end=" ")
"""


# 5️⃣ Count how many even numbers are between 1 and 50

"""
count = 0
for x in range(1,51):
    if x %2 == 0:
        count +=1
    
print(count," even number")

"""


"""🔹 LEVEL B — Medium Logic"""

# 6️⃣ Sum of digits of a number


# num = 123
# total = 0

# while num>0:
#     rev = num%10
#     total +=rev
#     num//=10

# print(total)


"""7️⃣ Count vowels in a string"""
# Take the character to check the string, and in is used in the if that check inside the varaible.
# value = "python programming"
# count = 0
# for ch in value:
#    if ch in "aeiou":
#       count +=1
# print(count) 


"""8️⃣ Check if a number is palindrome"""

# num= 126
# nnum = 0
# orginl= num

# while num>0:
#    rem = num % 10
#    nnum= nnum*10 + rem
#    num //=10


# if orginl == nnum:
#     print(orginl, "-> Palindrome")
# else:
#     print(orginl, "-> not palindrome")



"""9️⃣ Find factorial using loop"""
# num = 5
# fact = 1
# factnum = num
# while num>0:
#     fact *=num
#     num -=1
# """
# OR

# for x in range(1,num+1):
#     fact *=x
# print(fact)
# """
# print(factnum,"-> ",fact)



"""🔟 Print this pattern"""

# for i in range (1,6):
# # *(Multiple) the Number with the string, it will repeat the string that times of number.
#     print("*"*i)


"""🔹 LEVEL C — Strong Logic (Think Carefully)"""

# 1️⃣1️⃣ Find second largest number from 3 numbers

# def second_largest(a,b,c):
#     if (a > b and a < c) or (a < b  and a > c):
#         return a
#     elif (b > a and b < c) or (b < a and b > c ):
#         return b
#     else:
#         return c
# print(second_largest(10,20,30))


# 1️⃣2️⃣ Check if a number is prime


def Is_prime(num):
    if num <= 1:
        print(num,"is not prime number")
    else:
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
               is_prime = False
               break

        if is_prime:
            print(num,"is prime number")
        else:
            print(num,"is not prime number")
Is_prime(7)
    
