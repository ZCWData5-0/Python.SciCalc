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
        else:
            print("That is not a valid input.")
    print("Bye.")


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)

### WHAT does this idiom do?
#     ANSWER BELOW:     # Maybe some group research is in order.

#if__name__=='__main__' Allows You # to Execute Code
# When the File Runs as a Script, but Not When It’s Imported as a Module

if __name__ == '__main__':
    main()
