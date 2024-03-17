import tkinter as tk
<<<<<<< HEAD:lydias_guicalc.py
from lydias_calculator import Calculator
=======
from calculatorNat import Calculator
>>>>>>> f710998cad4d8f40df2be0654da60136d88e8dfd:guicalc.py

class CalcGUI:
    def __init__(self, master, engine):
        self.master = master
        self.engine = engine
        master.title("Zip Calculator")

        # Create the display widget
        self.display = tk.Entry(master, width=40, justify='right', font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("0", 4, 1)

        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)
        self.create_button(".", 4, 2)
        self.create_button("C", 4, 0)
        self.create_button("=", 5, 3)

        ## YOU need to add lots more buttons for the added funcs

        # Initialize the calculator state
        self.reset()

    def reset(self):
        self.operation = None
        self.first_number = 0
        self.display.delete(0, tk.END)

    def create_button(self, text, row, col):
        button = tk.Button(self.master, text=text, padx=10, pady=5, font=('Arial', 20), command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, text):
        if text.isdigit():
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current) + str(text))
        elif text == '.':
            current = self.display.get()
            if '.' not in current:
                self.display.insert(tk.END, '.')
        elif text == 'C':
            self.reset()
        elif text in ['+', '-', '*', '/']:
            self.first_number = float(self.display.get())
            self.operation = text
            self.display.delete(0, tk.END)
        elif text == '=':
            second_number = float(self.display.get())
            if self.operation == '+':
                self.engine.add(self.first_number, second_number)
                result = self.engine.value()
            elif self.operation == '-':
                self.engine.sub(self.first_number, second_number)
                result = self.engine.value()
            elif self.operation == '*':
                self.engine.mul(self.first_number, second_number)
                result = self.engine.value()
            elif self.operation == '/':
                self.engine.div(self.first_number, second_number)
                result = self.engine.value()
            self.reset()
            self.display.insert(0, str(result))


# main start
def main():
    calc_engine = Calculator()
    root = tk.Tk()
    calculator = CalcGUI(root, calc_engine)
    root.mainloop()
    # root.mainloop() pauses the execution of any further lines of code here

#
### WHAT does this idiom do?
# Maybe some group research is in order.
#
if __name__ == '__main__':
    main()
