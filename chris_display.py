import calculator

################################
#please de-comment this and paste it within the calculator.py Class calulator to full functionality! :)



#def set_value(self):
   # if self.currentValue == 0.0:
   #     x = float(input("Enter a value:"))
   #     self.currentValue = x

################################

from lydias_calculator import Calculator


def getNumber():
    try:
        a = float(input("Enter a number: "))
        return a
    except ValueError:
        a = float(input("Enter a number: "))
        return a

def displayResult(x: float):
     print(x, "\n")


def performCalcLoop(calc):
    displayResult(calc.value())
    calc.set_value(input("Enter a number: "))
    while True:
        displayResult(calc.value())
       # if calc.value == 0.0:
       #     calc.set_value(input("Enter a number: "))
        if calc.value == 0.0:
            displayResult(calc.value())
            calc.set_value(input("Enter a number: "))
        choice = input("Operation? ").lower()
        if choice == 'q':

            break  # user types q to quit calulator.
        elif choice == 'c' or choice.__contains__('cl'):
            calc.clear()
            calc.set_value(input("Enter a number: "))
        elif choice == '+' or choice.__contains__('add') or choice.__contains__('plu'):

            break  # user types q to quit calculator.
        elif choice == '+':
            a = getNumber()
            calc.add(calc.value(), a)
        elif choice == '-' or choice.__contains__('sub') or choice.__contains__('min'):
            a = getNumber()
            calc.sub(calc.value(), a)
        elif choice == '*' or choice.__contains__('mul') or choice.__contains__('times'):
            a = getNumber()
            calc.mul(calc.value(), a)
        elif choice == '/' or choice.__contains__('div'):
            a = getNumber()
            calc.div(calc.value(), a)
        elif choice == 'square' or choice == 'sq' or choice == 'sqre':  # my code
            calc.square()
        elif choice == 'square root' or choice == 'sqrt':  # my code
            calc.square_root(calc.value())
        elif choice == 'factorial' or choice.__contains__('fa'):
            calc.factorial(calc.value())
        elif choice.__contains__('ss') and not choice.__contains__('mul'):
            calc.inverse_of_number2(calc.value())
        elif choice.__contains__('mi') or choice.__contains__('mul'):
            calc.inverse_of_number2(calc.value())

        elif choice == 'h':
            calc.calc_menu()
        else:
            print("That is not a valid input.")
    print("Bye.")


# main start
def main():
    calc = Calculator()
    #calc1 = Calculator()
   # print(calc.getTrigUnitMode())
    #print(calc1.getTrigUnitMode())
    #calc1.switchUnitsMode()
    #print(calc.getTrigUnitMode())
   # print(calc1.getTrigUnitMode())

    # print(calc.getTrigUnitMode())
    # calc.switchUnitsMode('degrees')
    # print(calc.getTrigUnitMode())
    # calc.switchUnitsMode('deges')
    # print(calc.getTrigUnitMode())
    calc.calc_menu()
    performCalcLoop(calc)

if __name__ == '__main__':
    main()