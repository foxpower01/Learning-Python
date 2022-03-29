import tkinter as tk

window = tk.Tk()

entName = tk.Entry(width=40)
entName.insert(tk.END, "what is your name?")
entName.pack()

window.mainloop()