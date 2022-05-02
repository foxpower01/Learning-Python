import tkinter as tk

turn = "X"

window = tk.Tk()

# def handle_click(event):

for i in range(3):
    for j in range(3):

        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)



window.mainloop()