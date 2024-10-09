import tkinter as tk
from math import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(str(screen.get()))
            screen_var.set(value)
        except Exception as e:
            screen_var.set("Error")
            screen.update()
    elif text == "C":
        screen_var.set("")
        screen.update()
    else:
        screen_var.set(screen_var.get() + str(text))
        screen.update()

root = tk.Tk()
root.geometry("500x600")
root.title("Scientific Calculator")

screen_var = tk.StringVar()
screen_var.set("")

screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, relief=tk.SUNKEN)
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

# Button Texts for Scientific Calculator Layout
buttons = [
    ['C', '√', '^', '+'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '/'],
    ['0', '.', '(', ')'],
    ['sin', 'cos', 'tan', 'log'],
    ['ln', 'π', 'e', '=']
]

for row in buttons:
    frame_row = tk.Frame(button_frame)
    frame_row.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for btn_text in row:
        btn = tk.Button(frame_row, text=btn_text, font="lucida 15 bold", relief=tk.RAISED, bd=5, padx=10, pady=10)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", click)

root.mainloop()