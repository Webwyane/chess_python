import tkinter as Tk
import tkinter as tk
from tkinter import ttk
            

class MyApplication1(tk.Tk):
    """Hello World Main Application"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        blocks=[]
        for i in range(8):  
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                label = tk.Label(self, width=8, height=4, relief="solid",bg=color)
                self.title("Chessboard")
                blocks.append(label)  
                label.grid(row=j, column=i )
if __name__ == '__main__':
    app = MyApplication1()
    app.mainloop()