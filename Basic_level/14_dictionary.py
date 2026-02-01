"""✅ Task 1

Create a dictionary student with:

name → "Ali"

age → 21

marks → 85

👉 Print the dictionary"""


# student ={
#     "name": "Ali",
#     "age":21,
#     "marks":85
# }
# print(student)

"""🔹 PART 2: Access Nested Dictionary
✅ Task 2

Create a nested dictionary:"""

student={
    "name":"Ali",
    "marks":{
        "math":80,
        "science":90
    }
}

# print(student["marks"]["science"])


"""PART 3: Update Nested Value
✅ Task 3

Using the above dictionary:
👉 Change math marks from 80 to 95
👉 Print updated dictionary"""

# student["marks"]["math"]=95
# print(student)


"""PART 4: Dictionary Methods
✅ Task 4

Print all keys

Print all values

Print all items"""

# d = {"a":10,"b":20,"c":30}
# print((d.keys()))
# print(d.values())
# print(d.items())


"""PART 5: Safe Access (get())
✅ Task 5

👉 Print "city" using get()
👉 Default value should be "Not Found"
"""
# person ={"name":"Sara","age":25}
# print(person.get("city","Not found"))


"""PART 6: Loop Through Dictionary
✅ Task 6
"""
# scores = {"Math":90,"English":85,"Science":88}
# for subject,marks in scores.items():
#     print(subject ,"->",marks)



# d = {"x":1,"y":2}
# d["z"]=3
# print(d)


# data ={}
# keys =["a","b","c"]
# for k in keys:
#     data[k] = 0
# print(data)

# Use fromkeys()

# dic = {
#     "cat":"a small animal",
#     "table":("a piece of furniture","list of facts & figures")
# }

# print(dic)


marks ={}

x  = int(input("Phy marks: "))
marks.update({"phy":x})


x  = int(input("Chem marks: "))
marks.update({"chem":x})

x  = int(input("Math marks: "))
marks.update({"math":x})

print(marks)
