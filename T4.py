# '''
# 1. Write a program to reverse a string.
# Sample input: “1234abcd”
# Expected output: “dcba4321”
# '''
# print('''Ans of Q1
# #####################################################################################''')

# a = input("Enter any string: ")
# # by loop
# revSt = ""
# for i in a:
#     revSt = i + revSt
# print(f"reverse string by loop: {revSt}")

# # by slicing

# revSt = a[::-1]
# print(f"reverse string by slicing: {revSt}")

# '''
# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12
# '''

# print("")
# print('''Ans of Q2
# #####################################################################################''')

# a = input("Enter any string: ")
# lowerCount,upperCount = 0,0

# for i in a:
#     if (i.isupper()):
#         upperCount += 1
#     elif (i.islower()):
#         lowerCount +=1
# print(f"No. of Uppercase characters : {upperCount}, No. of Lower case Characters : {lowerCount}")

# '''
# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
# '''
# print("")
# print('''Ans of Q3
# #####################################################################################''')

# def uniqueElement(x):
#     a = set(x)
#     return list(a)

# x = [1, 5, 10, 15,5,2, 1, 0, 3, 10]
# a = uniqueElement(x)
# print(a)

# '''
# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# '''
# print("")
# print('''Ans of Q4
# #####################################################################################''')

# a = input ("Enter a hyphen-separated sequence of words: ")
# words = a.split('-')
# words.sort()
# #  Using built in join function
# a = '-'.join(words)
# print(a)
# # using loop
# a = ""
# for i in words:
#     a = a + str(i) + "-"
# a = a[:-1]
# print(a)


# '''
# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Sample input: Hello world Practice makes man perfect
# Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT
# '''
# print("")
# print('''Ans of Q5
# #####################################################################################''')
# text = input("Enter your text here:")
# text = text.upper()
# print(f"your input in upper case:\n{text}")

# '''
# 6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.
# '''
# print("")
# print('''Ans of Q6
# #####################################################################################''')

# def add(a,b):
#     return int(a) + int(b)

# a = '5'
# b = '10'
# print(f"sum of {a} and {b} = {add(a,b)}")

# '''
# 7. Define a function that can accept two strings as input and print the string with the maximum length in the console. If two strings have the same length, then the function should print both the strings line by line.
# '''

# from operator import le
# from queue import PriorityQueue


# print("")
# print('''Ans of Q7
# #####################################################################################''')

# def printMaxLenght(a,b):
#     if(len(a)>len(b)):
#         print(f"Longest String (count:{len(a)})")
#         print(a)
#     if(len(a) == len(b)):
#         print(f"Longest String (count:{len(a)})")
#         print(a)
#         print(b)
#     else:
#         print(f"Longest String (count:{len(b)})")
#         print(b)

# a = input("Enter the string 1: ")
# b = input("Enter the string 2: ")
# printMaxLenght(a,b)

# '''
# 8. Define a function which can generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included).
# '''

# print("")
# print('''Ans of Q8
# #####################################################################################''')

# def squareTuple():
#     sqList = []
#     for i in range(1,21):
#         sqList.append(i ** 2)
#     return tuple(sqList)    

# x = squareTuple()
# print(x)

# '''
# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
# '''
# print("")
# print('''Ans of Q9
# #####################################################################################''')

# def showNumbers(limit):
#     for i in range(limit+1):
#         print(f"{i} {'EVEN'if i%2 == 0 else 'ODD'}")

# a = int(input("Enter the limit to print ODD/EVEN number: "))
# showNumbers(a)


# '''
# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)
# '''
# print("")
# print('''Ans of Q10
# #####################################################################################''')

# a = [i for i in range(1,21)]
# z = lambda i:i%2 == 0
# evenNum = filter(z,a)
# print(list(evenNum))

# '''
# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the numbers in the filtered list. Use lambda() to define anonymous functions.
# '''

# print("")
# print('''Ans of Q11
# #####################################################################################''')

# myList = [i for i in range(1,11)]
# print(f"My List: {myList}")
# evenNum = list(filter(lambda x : x%2 == 0, myList))
# print(f"Even numbers: {evenNum}")
# squareNum = list(map(lambda x : x ** 2,evenNum))
# print(f"Square of that Even numbers: {squareNum}")

# '''
# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
# '''

# print("")
# print('''Ans of Q12
# #####################################################################################''')

# def div(a,b):
#     return a/b

# a = int(input("Enter numerator to perform Division: "))
# b = int(input("Enter denominator to perform Division: "))

# try:
#     print("Division of {} by {} is {:.2f}".format(a,b,div(a,b)))
# except Exception as e:
#     print(e)


# '''
# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
# '''

# from functools import reduce

# print("")
# print('''Ans of Q13
# #####################################################################################''')

# myList = [1,2,3,4,5,6,7]
# z = reduce(lambda x,y : str(x) + str(y),myList)
# print(z)

# '''
# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7. Make sure to use only higher order functions.
# '''

# print("")
# print('''Ans of Q14
# #####################################################################################''')

# def notDiv3(a):
#     temp = []
#     for i in a:
#         if i % 3 != 0 : temp.append(i) 
#     return temp

# def mul7AndDiv3(a):
#     x = notDiv3(a)
#     temp = []
#     for i in x:
#         if (i % 7 == 0):
#             temp.append(i)
#     return temp
            
# a = int(input("Upto which number that need to find out the values are not divisible by 3 but are a multiple of 7: "))
# myList  = [i for i in range(1,a+1)]

# print(f"From the list: {myList}\nThe values which are not divisible by 3 but are a multiple of 7: {mul7AndDiv3(myList)}")

'''
15. Write a program in Python to multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.
'''

print("")
print('''Ans of Q15
#####################################################################################''')

def mulItslef(x):
    return x * x

myList = [i for i in range(1,21)]

ouptputList = list(map(mulItslef,myList))
print(f"My List: {myList}")
print(f"Output List: {ouptputList}")

