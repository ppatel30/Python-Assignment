# '''
# 1. Write a program in Python to perform the following operation:
# - If a number is divisible by 3 it should print “Consultadd” as a string
# - If a number is divisible by 5 it should print “Python Training” as a string
# - If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
# '''
# print('''Output of Q1
# #########################################################################################''')

# a = int(input("Enter any number: "))
# b= 0
# if (a%3 == 0):
#     if (a%5 == 0):
#         print("Consultadd - Python Training")
#     else:
#         print("Consultadd")
# elif (a%5 == 0):
#     print("Python Training")

# '''
# 2. Write a program in Python to perform the following operator based task:
# - Ask user to choose the following option first:
#     If User Enter 1 - Addition
#     If User Enter 2 - Subtraction
#     If User Enter 3 - Division
#     If User Enter 4 - Multiplication
#     If User Enter 5 - Average
# - Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above.
# - Ask the user to enter two more numbers as first and second for calculating the average as
# soon as the user chooses an option 5.
# - At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
# NOTE: At a time a user can only perform one action.
# '''

# print("")
# print('''Output of Q2
# #########################################################################################''')

# user_in = int(input('''Enter 1 - Addition
#     Enter 2 - Subtraction
#     Enter 3 - Division
#     Enter 4 - Multiplication
#     Enter 5 - Average
#     Note:select only one option at time
#     your selection: 
#     '''))
# if (user_in in range(1,5)):
#     num1 = int(input("Enter the number 1: "))
#     num2 = int(input("Enter the number 2: "))
# elif(user_in == 5):
#     first = int(input("Enter the first number: "))
#     second = int(input("Enter the second number: "))
# else:
#     print("choose correct number")

# if(user_in == 1):
#     z = num1+num2
# elif(user_in == 2):
#     z = num1-num2
# elif(user_in == 3):
#     z = num1/num2
# elif(user_in == 4):
#     z = num1*num2
# elif(user_in == 5):
#     z = (first+second)/2

# if(z<0):
#     print("NEGATIVE")

# '''
# 3. Program as per given flow chart
# '''

# print("")
# print('''Output of Q3
# #########################################################################################''')

# a = 10
# b = 20
# c = 30

# avg = (a +b +c)/3
# print(f"avg ={avg}")

# if(avg > a and avg > b and avg > c):
#     print("avg is higher than a,b,c")
# else:
#     if(avg > a and avg > b):
#         print("avg is higher than a,b")
#     else:
#         if(avg > a and avg > c):
#             print("avg is higher than a,c")
#         else:
#             if(avg > b and avg > c):
#                 print("avg is higher than b,c")
#             else:
#                 if(avg > a):
#                     print("avg is just higher than a")
#                 else:
#                     if(avg > b):
#                         print("avg is just higher than b")
#                     else:
#                         if(avg > c):
#                             print("avg is just higher than c")

# '''
# 4. Write a program in Python to break and continue if the following cases occurs:
# - If user enters a negative number just break the loop and print “It’s Over”
# - If user enters a positive number just continue in the loop and print “Good Going”
# '''
# print("")
# print('''Output of Q4
# #########################################################################################''')

# while(True):
#     a = int(input("Enter any number: "))
#     if (a<0):
#         print("It’s Over")
#         break
#     print("Good Going")
    
    
# '''
# 5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200.

# '''
# print("")
# print('''Output of Q5
# #########################################################################################''')

# result = []
# for num in range(2000,3201):
#     if(num % 7 == 0 and num % 5 != 0):
#         result.append(num)

# print(result)

# ''''
# 7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
# Note: Use ‘continue’ statement
# '''

# print("")
# print('''Output of Q7
# #########################################################################################''')

# s = ""
# for i in range(7):
#     if (i == 3 or i == 6):
#         continue
#     s = s + str(i) + " "  
# print(s)

# '''
# 8. Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
# Sample input: consul72
# Expected output: Letters 6 Digits 2
# '''

# print("")
# print('''Output of Q8
# #########################################################################################''')

# d,s = 0,0
# st = input ("Enter the Alpha numeric: ")
# for i in st:
#     if(i.isalpha()):
#         s += 1
#     elif(i.isnumeric()):
#         d += 1

# print(f"Letters {s} Digits {d}")

# '''
# 9. Read the two parts of the question below:
# - Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.
# - Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. (The program continues as long as a user has not answered “no” and has not guessed the correct number)
# '''
# print("")
# print('''Output of Q9
# #########################################################################################''')

# '''
# part 1:

# number = 780
# while(True):
#     answer = int(input("guess the lucky number: "))
#     if (answer == number):
#         break
# '''
# # Adding Part 2: 

# number = 780
# while(True):
#     answer = int(input("guess the lucky number: "))
#     if (answer == number):
#         break
#     else:
#         r = input("do you want to guess again (Y/N): ")
#         if (r.lower() == 'y'):
#             continue
#         elif (r.lower() == 'n'):
#             break


# '''
# 10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
# such as
# counter = 1
# While counter <= 5:
#     print(“Type in the”, counter, “number”
#     counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the
# correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
# After the fifth guess it stops and prints “Game over!”.
# '''

# print("")
# print('''Output of Q10
# #########################################################################################''')

# number = 480
# counter = 1
# while (counter <= 5):
#     answer = int(input("guess the lucky number: "))
#     if(answer == number):
#         print("Good guess!")
#     else:
#         if(counter < 5):
#             print("Try again!")
#     counter=counter+1
# print("Game over!")

'''
11. In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.
'''
print("")
print('''Output of Q11
#########################################################################################''')

number = 480
counter = 1
while (counter <= 5):
    answer = int(input("guess the lucky number: "))
    if(answer == number):
        print("Good guess!")
        break
    else:
        if(counter == 5):
            print("Sorry but that was not very successful")
        else:
            print("Try again!")
    counter=counter+1
    



