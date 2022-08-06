'''
1. Write a program that calculates and prints the value according to the given formula:
Q= Square root of [(2*C*D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
D is a variable whose values should be input to your program in a comma-separated sequence
'''
# from math import sqrt

# def Q(D, C= 50, H =30):
#     return sqrt((2*C*D)/H)

# a = int(input("Enter the number: "))
# Output = Q(a)
# # Output =sqrt(a)
# print(f"Output of Square root of [(2*C*D)/H] where C = 50 and H =30: {Output:.4f}")


'''
2. Define a class named Shape and its subclass Square. The Square class has an init function whichtakes length as argument. Both classes have an area function which can print the area of the shapewhere Shape’s area is 0 by default. 
'''
# print("")
# print('''Ans of Q2
# ############################################################################################''')

# class Shape:
#     def area(self):
#         print("Shape is not define, default is 0")
#         return 0


# class Square(Shape):
#     def __init__(self,length):
#         self.length = length

#     def area(self):
#         print(f"Area of square is : {self.length * self.length}")
#         return self.length * self.length

# Sq1 = Square(5)
# S1 = Shape()
# Sq1.area()
# S1.area()

'''
3. Create a class to find three elements that sum to zero from a set of n real numbers
Input array: [-25,-10,-7,-3,2,4,8,10]
Expected output: [[-10,2,8],[-7,-3,10]]
'''
# print("")
# print('''Ans of Q3
# ############################################################################################''')

# class FindSum0:
#     def __init__(self,x):
#         self.x = x
#         self.y = x
#         self.z = x
#         self.output = []
#         self.count = 0
    
#     def FindComb(self):
#         for i in self.x:
#             for j in self.y[1:]:
#                 for k in self.z[2:]:
#                     if (i + j + k == 0):
#                         temp = set([i,j,k])
#                         if len(temp) == 3:
#                             temp = list(temp)
#                             if self.output.count(temp) == 0:
#                                 self.count = self.count + 1
#                                 self.output.append(temp)
#         return self.output


# a = input("Enter the comma seprated numbers: ")
# b = a.split(",")
# b = list(set([int(i) for i in b]))
# print(b)
# obj = FindSum0(b)
# print(obj.FindComb())


'''
4. Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minute.
'''
# print("")
# print('''Ans of Q4
# ############################################################################################''')

# class Time:
#     def __init__(self,hours,minutes):
#         self.hours = hours
#         self.minutes = minutes
    
#     def addTime(self,other):
#         hr = self.hours + other.hours
#         min = self.minutes + other.minutes
#         if min == 60:
#             hr += 1
#             min = 0
#         elif min == 120:
#             hr += 2 
#             min = 0
#         elif min > 60:
#             hr += 1
#             min = min - 60  
#         return Time(hr, min)

#     def displayTime(self):
#         print(f"Total time is {self.hours} hours, {self.minutes} minutes")

#     def displayMinute(self):
#         self.minutes =  (self.hours * 60) + self.minutes
#         print(f"Total time in minutes is {self.minutes}")

# # Time (Hr,min)
# T1 = Time(1,2)
# T2 = Time(2,1)
# T3 = T1.addTime(T2)
# T3.displayTime()
# T3.displayMinute()


'''
5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a parameter. The constructor must assign the integer value to the age variable after confirming the argument passed is not negative; if a negative argument is passed then the constructor should set age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance methods:
- yearPasses() should increase age by the integer value that you are passing inside the function.
- amIOld() should perform the following conditional actions:
    - If age is between 0 and <13, print “You are young”.
    - If age is >=13 and <=19 , print “You are a teenager”.
    - Otherwise, print “You are old”.
'''

class Person:
    def __init__(self, age):
        if (age >= 0):
            self.age = int(age)
        else:
            self.age = 0
            print("Age is not valid, setting age to 0")

    def yearPass(self, x):
        self.age += int(x)
        return self.age

    def amIOld(self):
        if(self.age > 0 and self.age < 13): 
            print("You are young")
        elif(self.age >= 13 and self.age <= 19):
            print("You are a teenager")
        else:
            print("You are old")


p1 = Person(10)
p1.yearPass(10)
p1.amIOld()

p2 = Person(-4)
p2.yearPass(22)
p2.amIOld()




