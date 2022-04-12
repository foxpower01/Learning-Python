import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

def convert():
    output = (int(ent_temp.get()) - 32) * (5 / 9)
    lbl_out["text"] = f"{output} \N{DEGREE CELSIUS}"

ent_temp = tk.Entry()
ent_temp.grid(row=0, column=0)

lbl_in = tk.Label(text="\N{DEGREE FAHRENHEIT}")
lbl_in.grid(row=0, column=1)

lbl_out = tk.Label(text="O \N{DEGREE CELSIUS}")
lbl_out.grid(row=0, column=3)

btn_run = tk.Button(text="\N{RIGHTWARDS BLACK ARROW}", command=convert)
btn_run.grid(row=0, column=2)

window.mainloop()