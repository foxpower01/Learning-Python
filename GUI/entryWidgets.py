import tkinter as tk

turn = "X"

window = tk.Tk()

def handle_click(event):
    button["text"] = turn

for i in range(3):
    for j in range(3):

        window.columnconfigure(i, weight=1, minsize=75)
        window.rowconfigure(i, weight=1, minsize=50)

        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        button = tk.Button(master=frame, text=f"Row {i}\nColumn {j}")
        button.bind("<Button-1>", handle_click)
        button.pack(padx=5, pady=5)

window.mainloop()