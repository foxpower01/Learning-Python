from email import header
from string import whitespace
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text = "hello world",
    foreground="white",
    background="black", 
    width=50,
    height=10)
clickMe = tk.Button(
    text="click me!",
    width=50,
    height=10,
    bg="red",
    fg="black"
)
greeting.pack()
clickMe.pack()
window.mainloop()