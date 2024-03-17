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
        if choice == 'q' or 'quit':
            break  # user types q to quit calulator.
        elif choice == 'c' or 'clear':
            calc.clear()
        elif choice == '+' or 'add':
            a = getNumber()
            calc.add(calc.value(), a)
        elif choice == '-' or 'subtract' or 'sub':
            a = getNumber()
            calc.sub(calc.value(), a)
        elif choice == '*' or 'multiply' or 'mul':
            a = getNumber()
            calc.mul(calc.value(), a)
        elif choice == '/' or 'divide' or 'div':
            a = getNumber()
            calc.div(calc.value(), a)
        elif choice == 'square' or '^2':  # my code
            calc.square(calc.value())
        elif choice == 'square root' or 'sqrt':  # my code
            calc.square_root(calc.value())
        elif choice == 'factorial' or 'fact':
            calc.factorial(calc.value())
        else:
            print("That is not a valid input.")
    print("Bye.")


# main start
def main():
    calc = Calculator()
    calc1 = Calculator()
    print(calc.getTrigUnitMode())
    print(calc1.getTrigUnitMode())
    calc1.switchUnitsMode()
    print(calc.getTrigUnitMode())
    print(calc1.getTrigUnitMode())

    # print(calc.getTrigUnitMode())
    # calc.switchUnitsMode('degrees')
    # print(calc.getTrigUnitMode())
    # calc.switchUnitsMode('deges')
    # print(calc.getTrigUnitMode())
    performCalcLoop(calc)

if __name__ == '__main__':
    main()