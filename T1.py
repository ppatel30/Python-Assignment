# '''
# 1. Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.
# '''

# a,b,c = 1,2.01,'string'
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# '''
# 2. Create a variable of type complex and swap it with another variable of type integer.
# '''
# # x = 1+2j
# # y = 5
# # print(x.real)

# '''
# 3. Swap two numbers using a third variable and do the same task without using any third variable.
# '''
# x = 5
# y = 10
# print(f" assigned values, x = {x} , y = {y}")

# z = x
# x = y
# y = z
# print(f"values after swap using third variable, x = {x} , y = {y}")

# x = 5
# y = 10
# print(f" assigned values, x = {x} , y = {y}")

# x , y = y, x
# print(f"values after swap whithout using third variable, x = {x} , y = {y}")




# '''
# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
# ''' 
# u_in = input("Enter your full name: ")
# print(f"your input = {u_in}")
# # for python 2.x
# #print "your input = {}".format(u_in)

# '''
# 5. Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the final output.
# '''
# a = int(input("Enter number between 1-10: "))
# b = int(input("Enter number between 1-10: "))
# z = a+b
# result = z+30
# print(f"Final output : {result}")

# '''
# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc
# '''

a = input("Enter anything: ")

# # with out eval function
# if (a == '0' or a == '1'):
#     print("Datatype of Entered value is Bool")
# elif (a.isdigit()):
#     if(a.count('.')==1):
#         print("Datatype of Entered value is float")
#     if(a.count('.')>1):
#         print("Consider Datatype of Entered value is string")
#     print ("Datatype of Entered value is int")
# else
#     print ("Datatype of Entered value is Str")

# #With the help of eval

# try:
#     x = type(eval(a))
#     print(f"The datatype of given value is {x}")
# except:
#     print(f"The datatype of given value is <class 'str'>")

# '''
# 7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
# '''
# # Upper CamelCase(Pastal Case)
# MyNameVar = "Parth"

# # Lower CamelCase(CamelCase)
# myNameVar = "Parth"

# # Snake CamelCase
# my_name_var = "Parth"

# # Upper Case
# MYNAMEVAR = "Parth"
'''
8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?
'''

'''
ANS: Yes, Value and datatype change to latest assigned vlaue and their datatype of any same variable in program, let see by the example below
'''
a = 5
a = "Parth"

print(a,type(a))