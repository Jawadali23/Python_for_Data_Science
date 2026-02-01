
""" for num in range(1,6):
    print(num)


for var in range(1,4):
    print("Hello word!")


x = 10
while x>0:
    print(x)
    x-=1



"""
# PART 2 — Medium Loop Practice

"""

for x in range (1,21):
    if x%2==0:
        print(x,end=" ")


total =0
for x in range(1,11):
    total+=x
print("Sum is: ",total)


x = 1
y = 5
while x<=10:
    result = x*y
    print(y,"x",x,"= ",result)
    x+=1

"""
# PART 3 — HARD LOOP PRACTICE

"""

num = 7
for x in range (1,11):
    print(num ,"x",x ,"= ", num *x)



num = 5
fact = 1
for x in range (1, num+1):
    fact *=x

print("5! = ",fact)
    


num = 12345
for digits in str(num):
    print(digits, end=" ")


num = 98765
count = 0

while num >0:
    count +=1
    num //=10
print('Total digits is: ', count)



num =123
rev = 0

while num>0:
    rem = num % 10
    rev = rev*10 +rem
    num //=10

print("Reversed Number: ",rev) 


num = 123
total = 0

while num > 0:
    total += num%10
    num //=10

print("Sum of digits: ", total)



for num in range (2, 51):
    isPrime = True
    for x in range (2, num):
        if num % x ==0:
            isPrime = False
            break
    if isPrime:
        print(num, end=" ")

"""

# While loop

# i = 1
# while i <= 100:
#     print(i)
#     i +=1

# i = 100
# while i >= 1:
#     print(i)
#     i -=1


# n = int(input("Enter number: "))
# i=1
# while i <=10:
#     print(n,"x",i,"= ",n*i)
#     i +=1


# nums = [10,20,30,40,50,60,70,80,90,100]
# heroies = ["batman","superman","ironman"]

# i = 0
# while i < len(heroies):
#     print(heroies[i])
#     i +=1

# nums = (10,20,30,40,50,60,70,80,90,100)

# x = 50
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#         i += 1
#         continue 
#         print("Found",i)
        
#     print("finding....",i)
#     i += 1



# For loop

# nums = (10,20,30,40,50,60,70,80,90,100)
# for nums  in range(1,101):
#     print(nums)


# 100 to 1
# step is for escape the number that are iteratable.
# for i in range(100,0,-1):
#     # print(i)
#     pass

# for x in range(120,1,-2):
#     print(x)

sum =0
num =0

while  num <=5:
    sum +=num
    num +=1
print("Total sum= ",sum)