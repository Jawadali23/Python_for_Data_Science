# import os
# os.remove("demo.txt")

# with open("demo.txt","a") as f:
#     f.write("for the file input and output")

# with open ("demo.txt","r") as f:
#     print(f.read())

# with open ("demo.txt","a+") as f:
    
#     print(f.read())
#     f.write("File I/O")


# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O")
#     f.write("\nusing Java.\nI like programming in Java.")
 


# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java","Python")
# print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)

# def check_word():
#     word = "learning"
#     with open( "practice.txt","r") as f:
#         data = f.read()
#         if (word in data):
#           print("Found")
#         else:
#           print("Not Found")

# check_word()


# def check_line():
#     word = "xlearning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no +=1
        
#     return -1

# print(check_line())


# def check_even():
#     count = 0
#     with open("practice.txt","r") as f:
#     # f.write("1, 2, 76, 84, 90, 101")
#         data = f.read()
#         nums = data.split(",")
#         for val in nums:
#             if(int(val) % 2 ==0):
#                 count +=1
#     print(count)
# check_even()


# with open ("data.txt","r") as f:
#     # print(f.read())
#     print(f.readline())


# with open("notes.txt","w") as f:
#     f.write("Python\nData Science\nAI")
#     f.write("Python\nData Science\nAI")


# with open("notes.txt","a") as f:
#     f.write("\nMachine Learning")

# with open("notes.txt","r+") as f:
#     print(f.read())
#     f.write("End of file")

# with open("sample.txt","w+") as f:
#     f.write("Learning Python")
#     f.seek(0)
#     print(f.read())


# with open("sample.txt","a+") as f:
#     f.write("\nFile Handling")
#     f.seek(0)
#     print(f.read())


