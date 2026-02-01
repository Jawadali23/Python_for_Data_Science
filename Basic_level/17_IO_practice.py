# with open("hello.txt","w") as f:
#     f.write("Hello Python")

# with open("hello.txt","r") as f:
#     print(f.read())


# with open("hello.txt","a") as f:
#     f.write("Learning File Handling")
        
    
# with open("hello.txt","r") as f:
#     count =0
#     data = f.read()
#     for val in data:
#         count +=1
    
#     print(count)


# with open("hello.txt","r") as f:
#     data = f.readline()
#     print(data)


# LEVEL 2: EASY–MEDIUM

# with open("profile.txt","w") as f:
#     f.write("Jawad Ali\n21\nData Scientist")

# with open("profile.txt","r") as f:
#     for line in f:
#         print(line.strip())

# line_no = 0   
# with open("profile.txt","r") as f:
#     for line in f: 
#         line_no += 1 
# print(line_no)

# import os
# os.remove("hello.txt")

# with open("profile.txt","r+") as f:
#     print(f.read())
#     f.write("\nPractice Completed")

# with open("hello.txt","w+") as f:
#     f.write("Hello, Everyone!")
#     f.seek(0)
#     print(f.read())


# with open("hello.txt","a+") as f:
#     f.write("\ntu kasi hai aap loga")
#     f.seek(0)
#     print(f.read())

# with open("notes.txt","r+") as f:
#     data = f.read()
#     new_data = data.replace("AI","Artificial Intelligence")
#     f.seek(0)
#     f.write(new_data)
#     # f.truncate()

# count = 0
# word = "Python"
# with open("notes.txt","r") as f:
#     data = f.read()
#     count = data.count(word)

#     print(count)
