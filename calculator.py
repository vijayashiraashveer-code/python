import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x450")
root.configure(bg="#1e1e1e")

expression= ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
def equal_press():
    global expression
    try:
          total = str(eval(expression))
        equation.set(total)
        expression = total 
        except ZeroDivisionError: 
             equation.set