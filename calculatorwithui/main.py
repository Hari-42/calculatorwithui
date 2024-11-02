import tkinter as tk
from tkinter import ttk

def append_to_display(char):
    current_expr = display_text.get()
    if char == '.':
        if '.' in current_expr.split()[-1]:
            return
    display_text.set(current_expr + str(char))


def evaluate_expression():
    try:
        expression = display_text.get()
        result = eval(expression)
        display_text.set(str(result))
    except Exception:
        display_text.set("Error")
        root.after(2000, clear_display)


def clear_display():
    display_text.set("")


def backspace():
    current_expr = display_text.get()
    display_text.set(current_expr[:-1])


def toggle_negative():
    current_expr = display_text.get()
    if current_expr:
        display_text.set(current_expr[1:] if current_expr[0] == '-' else '-' + current_expr)


def square_number():
    current_expr = display_text.get()
    try:
        result = float(current_expr) ** 2
        display_text.set(str(result))
    except ValueError:
        display_text.set("Error")
        root.after(2000, clear_display)


def handle_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        append_to_display(key)
    elif key == "\r":
        evaluate_expression()
    elif key == "\x1b":
        clear_display()
    elif key == "\b":
        backspace()
    elif key == "-":
        toggle_negative()



root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(True, True)


display_text = tk.StringVar()
display_entry = tk.Entry(root, textvariable=display_text, font=('Roboto', 20), bd=10, insertwidth=4, width=15,borderwidth=4, justify='right')
display_entry.grid(row=0, column=0, columnspan=4, sticky='nsew')


buttons = [
    'C', 'x²', 'Del', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '+/-', '0', '.', '='
]

row_num = 1
col_num = 0
for label in buttons:
    if label == '=':
        btn = ttk.Button(root, text=label, command=evaluate_expression, style='calc.TButton')
    elif label == 'C':
        btn = ttk.Button(root, text=label, command=clear_display, style='calc.TButton')
    elif label == 'Del':
        btn = ttk.Button(root, text=label, command=backspace, style='calc.TButton')
    elif label == '+/-':
        btn = ttk.Button(root, text=label, command=toggle_negative, style='calc.TButton')
    elif label == 'x²':
        btn = ttk.Button(root, text=label, command=square_number, style='calc.TButton')
    else:
        btn = ttk.Button(root, text=label, command=lambda key=label: append_to_display(key), style='calc.TButton')

    btn.grid(row=row_num, column=col_num, ipadx=10, ipady=10, padx=5, pady=5, sticky='nsew')

    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1


for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)


style = ttk.Style()
style.configure('calc.TButton', font=('Roboto', 18), padding=10)


root.bind('<Key>', handle_key)


root.mainloop()


