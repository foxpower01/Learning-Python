from random import randint
import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1], minsize=50)

def rollDie():
    lbl_value["text"] = randint(1, 6)

lbl_value = tk.Label(text="")
lbl_value.grid(row=1, column=0, sticky="nsew")

btn_roll = tk.Button(text="roll", command=rollDie)
btn_roll.grid(column=0, row=0, sticky="nsew")

window.mainloop()