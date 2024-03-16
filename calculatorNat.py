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
    # dec = 409 #need to feed the input to this variable
    #
    # print("The decimal value of", dec, "is:") #Ensure "Print" is going to Display
    # print(bin(dec), "in binary.")
    # print(oct(dec), "in octal.")
    # print(hex(dec), "in hexadecimal.")

    #Python program to convert decimal into other number systems

    #HOW TO ACTIVATE & MAKE BUTTON FOR THIS?

    # def displayModeBin(self):
    #     displayMode = self.currentValue  # WHAT GOES HERE? Need to feed the input to this variable
    #     return ("The decimal value of", displayMode, "is:")  # Ensure this is going to Display
    #     return (bin(displayModeBin), "in binary.")

    # def displayModeOct(self):
    #     displayMode = self.currentValue  # WHAT GOES HERE? Need to feed the input to this variable
    #     return ("The decimal value of", displayMode, "is:")  # Ensure this is going to Display
    #     return (oct(displayModeOct), "in octal.")
    #
    #
    # def displayModeDec(self):
    #     displayMode = self.currentValue  # WHAT GOES HERE? Need to feed the input to this variable
    #     return ("The decimal value of", displayMode, "is:")  # Ensure this is going to Display
    #     return (hex(displayMode), "in decimal.")
    #
    #
    # def displayModeHex(self):
    #     displayMode = self.currentValue  # WHAT GOES HERE? Need to feed the input to this variable
    #     return ("The decimal value of", displayMode, "is:")  # Ensure this is going to Display
    #     return (hex(displayMode), "in hexadecimal.")


# MASTER ORIGINAL
# def displayMode(self):
#     displayMode = self.currentValue  # WHAT GOES HERE? Need to feed the input to this variable
#
#     return ("The decimal value of", displayMode, "is:")  # Ensure this is going to Display
#     return (bin(displayMode), "in binary.")
#     return (oct(displayMode), "in octal.")
#     return (hex(displayMode), "in hexadecimal.")
