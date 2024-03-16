from lydias_calculator import Calculator


def getTwoNumbers():
    a = float(input("Enter your first number: "))
    b = float(input("Enter your second number: "))
    return a, b


def displayResult(c: Calculator):
    if c.currentValue is None:
        print(c.currentMsg)
    else:
        print(c.currentValue, "\n")


def performCalcLoop(calc):
    while True:
        choice = input("Operation? ")
        if choice == 'q':
            break  # user types q to quit calulator.
        elif choice == 'add':
            a, b = getTwoNumbers()
            calc.add(a,b)
            displayResult(calc)
            #displayResult(calc.add(a, b))
        elif choice == 'sub':
            a, b = getTwoNumbers()
            displayResult(calc.sub(a, b))
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
