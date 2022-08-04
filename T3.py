'''
1. Create a list of 10 elements of four different data types like int, string, complex and float.
'''
print ('''Ans of Q1
#####################################''')

x = [1 , 2.5, True, 5+6j, None, "Consultadd", (0,1), "25", 17, {'age':25}] 

for i in x:
    print(i, type(i))

'''
2. Create a list of size 5 and execute the slicing structure
'''
print("")
print ('''Ans of Q2
#####################################''')

x = ['Parth','Amit','Jeet','Parvinder','Ivan']
print(x[1:2])
print(x[:5])
print(x[2:])
print(x[-2:-4:-1])
print(x[-1::-2])
print(x[::-1])

'''
3. Write a program to get the sum and multiply of all the items in a given list.
'''
print("")
print ('''Ans of Q3
#####################################''')
#list of even number
from math import prod

x = [i for i in range(1,21) if i%2 == 0]
# sum of all item using loop
a = 0
for i in x:
    a = a+i
print(a)
# sum of all item using function
print(sum(x))

# Multiplication of all item using loop
a = 1
for i in x:
    a = a * i
print(a)

# Multiplication of all item using function
print(prod(x))

'''
4. Find the largest and smallest number from a given list.
'''

print("")
print ('''Ans of Q4
#####################################''')
# using loops - MAx value
mx = x[0]
for i in x:
    if (i > mx):
        mx = i
print(mx)
# using function - Max value
print(max(x))

# using loops - Min value
mn = x[0]
for i in x:
    if (i < mn):
        mn = i
print(mn)
# using function - min value
print(min(x))

'''
5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
'''

print("")
print ('''Ans of Q5
#####################################''')
x = [i for i in range(1,100)]

desiredList = []
for i in x:
    if (i%2 == 0):
        continue
    desiredList.append(i)
print(desiredList)

'''
6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
'''
print("")
print ('''Ans of Q6
#####################################''')

myList = []
for i in range(1,31):
    if (i <= 5 or i >=26):
        myList.append(i ** 2)
    else:
        myList.append(i)
print(myList)

'''
7. Write a program to replace the last element in a list with another list.
Sample input: [1,3,5,7,9,10], [2,4,6,8]
Expected output: [1,3,5,7,9,2,4,6,8]
'''
print("")
print ('''Ans of Q7
#####################################''')

x = [1,3,5,7,9,10]
y = [2,4,6,8]

x.pop()
x.extend(y)
print(x)

'''
8. Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}
'''

print("")
print ('''Ans of Q8
#####################################''')

a={1:10,2:20}
b={3:30,4:40}

a.update(b)
print(a)

'''
9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
'''
print("")
print ('''Ans of Q9
#####################################''')

n = int(input("Enter the size of dict with square value, n= " ))
sq = dict()
for i in range(1,n+1):
    sq.update({i:(i ** 2)})
print(sq)

'''
10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
'''
print("")
print ('''Ans of Q10
#####################################''')

inStr = input("Enter the comma-seprated numbers: ")
myList = inStr.split(',')
print(myList)
myTuple = tuple(myList)
print(myTuple)