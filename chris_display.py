import calculator

################################
#please de-comment this and paste it within the calculator.py Class calulator to full functionality! :)
#def set_value(self):
#    if self.currentValue == 0.0:
#        x = float(input("Enter a value:"))
#        self.currentValue = x
################################

from calculator import Calculator


def getNumber():
    a = float(input("enter number "))
    return a


def displayResult(x: float):
     print(x, "\n")


def performCalcLoop(calc):
    while True:
        displayResult(calc.value())
        calc.set_value()
        if calc.value == 0.0:
            displayResult(calc.value())
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == '+':
            a = getNumber()
            calc.add(calc.value(), a)
        elif choice == '-':
            a = getNumber()
            calc.sub(calc.value(), a)
        else:
            print("That is not a valid input.")
    print("Bye.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)

#
### WHAT does this idiom do?
# Maybe some group research is in order.
#


if __name__ == '__main__':
    main()