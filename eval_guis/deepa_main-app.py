from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


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
            displayResult(calc.square())
        elif choice == 'square root':          #my code
            displayResult(calc.square_root())
        elif choice == 'factorial':
            displayResult(calc.factorial())
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


#
### WHAT does this idiom do?
# Maybe some group research is in order.
#
if __name__ == '__main__':
    main()
