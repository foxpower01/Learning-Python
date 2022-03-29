import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Name")
entry = tk.Entry()
label.pack()
entry.pack()
input = entry.get()
entry.delete(0, tk.END)
input = tk.Label(text=input)
input.pack()
window.mainloop()