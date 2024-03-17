from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b

def getExponentNum():
    num = int(input("Enter the number for the power :"))
    return num

def displayResult(x: float):
    print(x, "\n")


def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            displayResult(calc.add(a, b))
        elif choice == 'sub':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
        elif choice == 'square':        #my code
            displayResult(calc.calculateSquare(calc.value()))
        elif choice == 'square root':          #my code
            displayResult(calc.calculateSquareRroot(calc.value()))
        elif choice == 'factorial':
            displayResult(calc.calculateFactorial(calc.value()))
        elif choice == 'exponent':
            num = getExponentNum()
            displayResult(calc.calculateExponent(calc.value(),num))
        elif choice == 'M+':
            calc.memoryAdd(calc.getMemVal(),calc.value())
        elif choice == 'M-':
            calc.memorySub(calc.getMemVal(),calc.value())
        elif choice == 'MR':  #Recall memory
            calc.setValue(calc.recallMemory())
            displayResult(calc.value())
        elif choice == 'MC':
            calc.clearMemory()
            displayResult(calc.value())

        else:
            print("That is not a valid input.")
    print("Bye.")


# main start
def main():
    calc = Calculator()
    calc1 = Calculator()
    # print(calc.getTrigUnitMode())
    # print(calc1.getTrigUnitMode())
    calc1.switchUnitsMode()
    # print(calc.getTrigUnitMode())
    # print(calc1.getTrigUnitMode())

    # print(calc.getTrigUnitMode())
    # calc.switchUnitsMode('degrees')
    # print(calc.getTrigUnitMode())
    # calc.switchUnitsMode('deges')
    # print(calc.getTrigUnitMode())
    performCalcLoop(calc)


#
### WHAT does this idiom do?
# Maybe some group research is in order.
#
if __name__ == '__main__':
    main()
