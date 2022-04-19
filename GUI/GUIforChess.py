import tkinter as tk

P = "P"

def setP(value):
    global P
    if value == '□':
        P = ''
    else:
        P = value

def createGUI(board):

    global P
    window = tk.Tk()
    window.title("Chess")

    for i in range(8):
        window.rowconfigure(i, minsize=40, weight=1)
        window.columnconfigure(i, minsize=40, weight=1)
        for j in range(8):
            if board:
                setP(board[i][j])
            match (i + j) % 2:
                case 0:
                    frame = tk.Frame(
                        master=window,
                        relief=tk.RAISED,
                        borderwidth=1,
                        bg="#8F8F8F"
                    )
                    frame.grid(row=i, column=j, sticky="nsew")
                    lbl_piece = tk.Label(frame, text=P, bg="#8F8F8F")
                    lbl_piece.pack(fill=tk.BOTH)
                case _:
                    frame = tk.Frame(
                        master=window,
                        relief=tk.RAISED,
                        borderwidth=1
                    )
                    frame.grid(row=i, column=j, sticky="nsew")
                    lbl_piece = tk.Label(frame, text=P)
                    lbl_piece.pack(fill=tk.BOTH)
            lbl_piece.bind("<Button>", handle_click)
    
    window.mainloop()
                
def handle_click(event):
    print(event)

def main():
    global P
    setP("hola")
    createGUI([['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['□', '□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□', '□'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']])

if __name__ == "__main__":
    main()