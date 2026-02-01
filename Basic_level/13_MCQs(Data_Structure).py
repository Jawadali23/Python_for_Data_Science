# LIST (Aliasing, Copy, Side Effects)

# 01 What is the output?
"""
lst = [1,2,3]
a = lst[:]
b = lst
a.append(4)
b.append(5)
print(lst)
"""

# 2️⃣ What is the output?
"""lst = [0]*3
lst[1]=5 
print(lst)
"""

# 3️⃣ What is the output?

lst =[[]] *3 
lst[1].append(1)
print(lst) 