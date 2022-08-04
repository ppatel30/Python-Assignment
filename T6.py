# '''
# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
# '''
# print('''Ans of Q1
# #####################################################################################''')

# a = input("Enter a string: ")

# UpperCaseChar = [i for i in a if i.isupper()]
# print(UpperCaseChar)

# '''
# 2. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects. The dictionary should map the students with their respective subjects. Let’s see how to do this using for loops and dictionary comprehension.
# HINT - Use Zip function also
# Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
# Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}
# '''
# print("")
# print('''Ans of Q2
# #####################################################################################''')

# studentName = ['Smit', 'Jaya', 'Rayyan']
# subjectName = ['CSE', 'Networking', 'Operating System']
# a = list(zip(studentName,subjectName))

# student = {}
# for i in a:
#     # student.update({i[0] : i[1]})
#     student[i[0]] = i[1]

# print(student)

# '''
# 4. Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
# '''
# print("")
# print('''Ans of Q4
# #####################################################################################''')

# def revStr(a):
#     for ch in a:
#         yield ch

# inStr = input("Input String = ")
# # next() calling evry iterable 
# # z = revStr(inStr)
# # outst = ""
# # for i in range(len(inStr)):
# #     outst = next(z) + outst
# # print(outst)

# # Using Genrator in loop
# outStr = ""
# for i in revStr(inStr):
#     outStr = i + outStr
# print(outStr)


'''
5. Write an example on decorators.
'''


print("")
print('''Ans of Q5
#####################################################################################''')

def HeaderFooter(func):
    def inner(x,y):
        print()
        print ("This is the Header")
        print()

        func(x,y)
        
        print()
        print("This is the footer")
        print()
    return inner

@HeaderFooter
def fullName(a,b):
    print((a + " " + b).upper())

a = input("Enter your first Name: ")
b = input("Enter your Last Name: ")
fullName(a,b)


