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
