import math
from math import *
from pprint import pprint


class Calculator:

    def __init__(self):
        self.currentValue = 0.0
        self.currentMsg = ""
        self.stored_value = 0.0
        self.menu_options = {
            "h": "help",
            "q": "quit",
            "+": "add",
            "-": "subtract",
            "*": "multiply",
            "/": "divide",
            "square": "square",
            "square root": "square root",
            "l": "common log",
            "il": "inverse common log",
            "ln": "natural log",
            "ex": "inverse natural log",
            "mi": "multiplicative inverse",
            "ss": "switch sign",
            "c": "clear display value",
            "m+": "save to memory",
            "mc": "reset memory",
            "mrc": "recall the current value from memory to the display",
            "sin": "sine",
            "cos": "cosine",
            "tan": "tangent",
            "is": "inverse sine",
            "ic": "inverse cosine",
            "it": "inverse tangent",
            "su": "switch units (degrees and radians",
            "sus": "set trig units to type",
            "fact": "factorial",

        }

    def __str__(self):
        return str(self.currentValue)

    def set_value(self, user_in):  # chris code
        if user_in == 'h':
            self.calc_menu()
            self.set_value(input("Enter a number: "))
        try:
            self.currentValue = float(user_in)
            # x = float(input("Enter a number:"))
            # self.currentValue = x
        except ValueError:
            print("nan")
            self.set_value(input("Enter a number: "))

    def calc_menu(self):
        pprint(self.menu_options)


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

    def div(self, x, y):
        try:
            value = x / y
            self.currentValue = value
        except ZeroDivisionError:
            self.currentValue = None
            self.currentMsg = 'DIV BY ZERO'

    def common_log(self, x):
        try:
            self.currentValue = math.log10(x)
        except ValueError:
            if x <= 0:
                self.currentValue = None
                self.currentMsg = 'NEG NUM ERROR'

    def inverse_common_log(self, x):
        self.currentValue = math.pow(10, x)

    def multiplicative_inverse(self):
        try:
            self.currentValue = 1 / self
        except ZeroDivisionError:
            if self == 0:
                self.currentValue = None
                self.currentMsg = 'DIV BY ZERO'

   # def inverse_of_number(self):
    #    try:
     #       if self != 0:
      #          self.currentValue = abs(self)
       # except ValueError:
        #    if self == 0:
         #       self.currentValue = None
          #      self.currentMsg = 'ZERO INVALID'

    def save_to_memory(self):
        self.stored_value = self.currentValue

    def reset_memory(self):
        self.stored_value = 0.0

    def recall_from_memory(self):
        self.currentValue = self.stored_value