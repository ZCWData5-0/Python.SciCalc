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
    try:
        a = float(input("Enter a number: "))
        return a
    except ValueError:
        a = float(input("Enter a number: "))
        return a

def displayResult(x: float):
     print(x, "\n")

def getExponentNum():
    num = int(input("Enter the number for the power :"))
    return num


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
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'c' or choice.__contains__('cl'):
            calc.clear()
            calc.set_value(input("Enter a number: "))
        elif choice == '+' or choice.__contains__('add') or choice.__contains__('plu'):
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
            calc.calculateSquare()
        elif choice == 'square root' or choice == 'sqrt':  # my code
            calc.calculateSquareRroot(calc.value())
        elif choice == 'factorial' or choice.__contains__('fa'):
            calc.calculateFactorial(calc.value())
        elif choice ==  'exponent' or choice == 'exp':
            calc.calculateExponent(calc.value(), getExponentNum())
        elif choice.__contains__('ss') and not choice.__contains__('mul'):
            calc.inverse_of_number2(calc.value())
        elif choice.__contains__('mi') or choice.__contains__('mul'):
            calc.inverse_of_number2(calc.value())
        elif choice == 'l':
            calc.common_log()
        elif choice == 'il':
            calc.inverse_common_log()
        elif choice == 'ln':
            calc.nat_log(calc.value())
        elif choice == 'ex':
            calc.in_nat_log(calc.value())
        elif choice == 'm+':
            calc.save_to_memory()
        elif choice == 'mc':
            calc.clearMemory()
        elif choice == 'mrc':
            calc.recallMemory()
        elif choice == 'sin':
            calc.get_sin(calc.value())
        elif choice == 'cos':
            calc.get_cos(calc.value())
        elif choice == 'tan':
            calc.get_tan(calc.value())
        elif choice == 'is':
            calc.get_asin(calc.value())
        elif choice == 'ic':
            calc.get_acos(calc.value())
        elif choice == 'it':
            calc.get_atan(calc.value())
        elif choice == 'h':
            calc.set_menu_value('h')

            #NATHAN ADDING DISPLAY OPTIONS - TWO CHAR DD -display Decimal / DO -display Octal / DH -display Hexidecimal / DB -display Binary
        elif choice == ('DD') or choice ==('dd') or choice == ('dD') or choice ==('Dd'):
                calc.displayModeDec()
        elif choice == ('DB') or choice == ('db') or choice == ('dB') or choice == ('Db'):
                calc.displayModeBin()
        elif choice == ('DO') or choice == ('do') or choice == ('dO') or choice == ('Do'):
                calc.displayModeOct()
        elif choice == ('DH') or choice == ('dh') or choice == ('dH') or choice == ('Dh'):
                calc.displayModeHex(calc.value())
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
    performCalcLoop(calc)

if __name__ == '__main__':
    main()