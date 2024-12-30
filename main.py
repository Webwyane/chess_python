import tkinter as Tk
import images 
from images import ChessImages
            

class MyApplication1(Tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.blocks={}
        self.title("Chessboard")
        self.create_chessboard()
        self.place_pawns()
    def create_chessboard(self):
        num=(1,2,3,4,5,6,7,8)
        abls = ("a", "b", "c", "d", "e", "f", "g", "h")
        for i in range(8):  
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                label = Tk.Label(self, width=8, height=4, relief="solid",bg=color,text=f"{abls[i]}{num[j]}",fg="green")
                self.blocks[f"{abls[i]}{num[j]}"] = label
                label.grid(row=j, column=i)

    def place_pawns(self):
        for col in "abcdefgh":  
            square = f"{col}2"  
            square1=f"{col}7"
            images_dir = r"E:\Games\pythonsid\python_chess\python_chess\pngs"
            chess_images = ChessImages(images_dir)
            chess_images.load_images()
            image_b_sol=chess_images.get_image("b_bdt")
            image_b_sol1=chess_images.get_image("w_blt")
            if square in self.blocks: 
                self.blocks[square].config(image=image_b_sol, text="") 
                self.blocks[square].image = image_b_sol  # Prevent garbage collection
            if square1 in self.blocks: 
                self.blocks[square1].config(image=image_b_sol1, text="") 
                self.blocks[square1].image = image_b_sol1  # Prevent garbage collection




if __name__ == '__main__':
    app = MyApplication1()
    app.mainloop()