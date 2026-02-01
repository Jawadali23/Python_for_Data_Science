"""# Task 1: Create a tuple
t1=(10,20,30,40)
print(t1)

# Task 2: Access elements
t=("Python","Java","C++","PHP")
print(t[0])
print(t[-1])


# Task 3: Loop through tuple
fruits = ("Apple","Banana","Cherry")

for fruit in fruits:
    print(fruit)

    
"""

# Task 4: Check item exists
# numbers = (2,4,6,8,10)
# if 6 in numbers:
#     print("Found")
# else:
#     print("Not Found")


# Task 5: count() method

# t=(5,1,5,2,5,3)

# print("5 repeats",t.count(5),"times")


# Task 6: index() method
"""
t=(10,20,30,40)
print(t.index(30))



tup=(1,2,3,4,5)
total = 0

for x in tup:
    total +=x
print("Sum of all elements: ",total)



# Create a tuple of 5 numbers.

t = (1,2,3,4,5)
print("Frist 3 elements: ",t[0:3])
print("Last 2 elements: ",t[-2:])

"""

# t=("Python","Java","C++","Python","Java")

# print(t.count("Python"))
# print(t.index("Java"))


# tup = (1,2,3,4,5,6,7,8,9,10)

# for x in tup:
#     if x % 2 ==0:
#         print(x,"Even number")


# t = (10,20,30,40,50)

# print(min(t))
# print(max(t))


# t = (1,2,3)
# t= t+(4,)
# # t[0]=10

# print(t)

# Reverse the elements
# t = (10,20,30,40,50)
# print(t[::-1])

# st = "Python"
# print(st[::-1])


# Palindrome 

t =(1,2,3,2,1)
rev=()
if t == t[::-1]:
    rev= t[::-1]
    print(rev,"Tuple is Palindrome")
else:
    print("Tuple is not Palindrome")