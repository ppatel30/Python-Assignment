# '''
# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
# '''

# print('''Ans of Q1
# #####################################################################################''')
# try:
#     x = eval('print("hello Word"')
# except SyntaxError as e:
#     print(e)

# '''
# 2. Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.
# '''
# import sys

# print("")
# print('''Ans of Q2
# #####################################################################################''')
# try:
#     f = open(f'{sys.argv[1]}',"r")
#     text = f.read()
#     print("File has been read successfully")
#     f.close()
# except:
#     print("Enter the correct file name, open again")

# '''
# 3. Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”
# '''
# print("")
# print('''Ans of Q3
# #####################################################################################''')

# try:
#     a = input("Enter the number: ")
#     b = int(a)
# except ValueError as e:
#     print("Enter the number only")
# else:
#     if len(a) > 4:
#         print("The length is too short/long !!! Please provide only four digits")

# '''
# 4. Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.
# '''

# print("")
# print('''Ans of Q4
# #####################################################################################''')

# LoginInfo = {
#     'Parth':'Parth1234',
#     'Sagar':'Sagar1234',
#     'Maitri':'Maitri1234',
#     'Mansi':'Mansi1234'
# }
# count = 0
# while (count < 3):
#     try:
#         userName = input("Enter the User name: ")
#         pass1 = input("Enter the Password: ")
#         pass2 = input("Re-Type the your Password: ")

#         if(pass1 == pass2):
#             if (LoginInfo.get(userName) == pass1):
#                 print("Login Successful")
#                 break
#             else:
#                 print("User name password incorrect")
#         else:
#             print("Both Password is not matched")
#         count += 1
#         if (count == 3):
#             print("You have reached maximum attempt")
#     except KeyError:
#         print("User name is not exist")

'''
6. Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present.
'''

print("")
print('''Ans of Q6
#####################################################################################''')

with open('doc.txt','r') as f:
    lineText = f.readlines()
for i in lineText:
    if ((len(i)-1)%2 == 0): #removed last '/n' character from lenghth
        print(i[:-1]) #removed last '/n' character
        