# remember, in Python classes are easier to use than Java.
#
from math import nan


class Calculator:

    def __init__(self):
        self.currentValue = 0.0

    def __str__(self):
        return str(self.currentValue)

    def clear(self):
        self.currentValue = 0.0

    # KRIS' clear function above, mine below.
    # Why did Kris give a clear function if we also had to?
    #
    #CLEAR
    # def clear(self, x, y):
    #     self.delete(0, 999)
    #     #youtube code was: txtDisplay.delete(0, END)
    #
    #CLEAR ALL
    # def clear_all(self, x, y):
    #     #clear text display (TEST THIS!)
    #     self.delete(0, 999)
    #     #youtube code was: txtDisplay.delete(0, END)

    def value(self):
        return self.currentValue

    # evaluation routines
    def add(self, x, y):
        self.currentValue = x + y

    def sub(self, x, y):
        self.currentValue = x - y

    def mul(self, x, y):
        self.currentValue = x * y
        #raise NotImplementedError

    def div(self, x, y):
        self.currentValue = x / y
        #raise NotImplementedError


    # Python program to convert decimal into other number systems
    dec = 409 #need to feed the input to this variable

    print("The decimal value of", dec, "is:") #Ensure "Print" is going to Display
    print(bin(dec), "in binary.")
    print(oct(dec), "in octal.")
    print(hex(dec), "in hexadecimal.")



        #reinitialize all variables
        #global first_number, second_number, Operation, Final_answer
        #first_number = 0
        #second_number = 0
        #Operation = 0
        #Final_answer = 0

# add lots more methods to this calculator class.

# IMPERFECT(?) Python code to demonstrate the working of
# degrees() and radians()

# importing "math" for mathematical operations
#import math

# a = math.pi/6
# b = 30
#
# # returning the converted value from radians to degrees
# print ("The converted value from radians to degrees is : ", end="")
# print (math.degrees(a))
#
# # returning the converted value from degrees to radians
# print ("The converted value from degrees to radians is : ", end="")
# print (math.radians(b))
