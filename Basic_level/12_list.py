"""🔹 Task 1: Create & Print

👉 Create a list of 5 numbers
👉 Print the list
"""

# lst = [10,20,30,40,50]
# print(lst)


"""Task 2: Access Elements"""

# lst = ["Python","Java","C++","PHP"]
# print("First Element ",lst[0])
# print("Last Element ",lst[-1])


"""Task 3: Modify List (Important Difference from Tuple)
👉 Change 30 to 300
👉 Print the list
"""
# numbers =[10,20,30,40]
# numbers [2]= 300
# print(numbers)


"""Task 4: Loop through list

👉 Create a list of fruits
👉 Print each fruit using a loop
"""

# fruits =["Apple","Banana","Cherry","Mango"]
# for frts in fruits:
#     print(frts)


"""Task 5: Check item exists
Check whether 6 exists
Print "Found" or "Not Found"
"""

# lst=[2,4,6,8,10]
# if 6 in lst:
#     print("Found")
# else:
#     print("Not Found")


"""Task 6: append()

👉 Create an empty list
👉 Add 3 numbers using append()
👉 Print the list
"""


# lst = [ ]
# lst.append(10)
# lst.append(20)
# lst.append(52)
# print(lst)


"""Task 7: pop()

👉 Remove the last element
👉 Print the list"""

# lst = [10,20,30,40]
# lst.pop()
# print(lst)

"""Task 8: insert()

👉 Insert 3 at the correct position"""

# lst = [1,2,4,5,6]
# lst.insert(2,3)
# print(lst)


""" List Methods """

"""Task 1: remove() vs pop()
👉 Remove 30 using remove()
👉 Remove the last element using pop()
👉 Print the final list
"""

# lst = [10,20,30,40,50]
# lst.remove(30)
# lst.pop()
# print(lst)


"""Task 2: sort()
👉 Sort the list in:
Ascending order
Descending order
"""

# nums = [5,2,9,1,7]
# # Ascending order
# nums.sort()
# print(nums)
# # Descending order
# nums.sort(reverse=True)
# print(nums)

"""🔹 Task 3: reverse()
👉 Reverse the list using reverse()
👉 Print the list
"""

# lst  = [10,20,30,40]
# lst.reverse()
# print(lst)

"""🔹 Task 4: List Slicing
👉 Print:
First 3 elements
Last 2 elements
Middle elements
"""

# lst =[1,2,3,4,5,6,7]

# print(lst[:3])
# print(lst[-2:])
# print(lst[1:-1]) -1 is greater than -2  like 6 > 5


"""Task 5: Count occurrences

👉 Count how many times 2 appears"""

# lst = [1,2,3,2,4,2,5]
# # lst.count(2)
# print(lst.count(2),'times 2 appears')


"""Task 6: Clear list

👉 Remove all elements from the list
"""

# lst = [10,20,30]
# lst.clear()
# print(lst)

""" BONUS
👉 Why this works:"""

# lst = [1,2,3]
# lst.append(4)
# print(lst,"Because the list is the mutable so that we add the last elements using the append method")

# t =(1,2,3)
# new_tple =t +(4,)

# print(new_tple)


"""Level 1: Basics (Warm-up)
1️⃣ Create & Access
"""

# nums = [10,20,30,40]

# print(nums[0])
# print(nums[-1])

"""2️⃣ Modify List"""

# nums = [1,2,3]
# nums[0] =99
# print(nums)

"""3️⃣ Length of List"""

# items = ["a","b","c"]
# print(len(items))

"""🔁 Level 2: Methods Practice
4️⃣ append vs extend"""

# lst = [1,2]
# # Add as single element in the list
# lst.append([3,4])
# print(lst)
# # Adds multiple element individually
# lst.extend([5,6])
# print(lst)

"""5️⃣ insert"""

# lst = [10,20,30]
# lst.insert(1,99)
# print(lst)

"""6️⃣ pop"""

# lst = [5,10,15]

# x = lst.pop()

# print(x, lst)


"""🔄 Level 3: Looping & Logic
7️⃣ Sum of elements
"""
# nums = [1,2,3,4]
# total = 0

# for x in nums:
#     total +=x
# print("Sum is ",total)

"""8️⃣ Count even numbers"""

# nums = [10,15,20,25,30]
# count = 0
# for x in nums:
#     if x % 2 ==0:
#         count+=1
# print(count)


"""9️⃣ Reverse a list (without reverse())"""

# nums= [1,2,3,4]
# print(nums[::-1])



"""🧪 Level 4: Tricky / Interview MCQs
🔟 What will be printed?"""

# lst = [1,2,3]
# new_lst = lst
# new_lst.append(4)
# print(new_lst)


"""1️⃣1️⃣ Output?"""
# print([1,2]*3)

"""1️⃣2️⃣ Shallow Copy vs Deep Copy"""

# a =[[1,2],[3,4]]
# b = a.copy()
# b[0][0]= 99
# print(a)

# import copy
# a = [1,2,[3,4]]
# b = a.copy()
# # a[2].append(5)
# print(a)
# print(b)

# print(a is b)
# print(a[2] is b[2])

# b = copy.deepcopy(a)
# a[2].append(5)
# print(a)
# print(b)

