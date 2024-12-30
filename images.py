import tkinter as Tk
from pathlib import Path

class ChessImages:
    def __init__(self, images_dir):
        self.images_dir = Path(images_dir)
        self.pieces = {}

    def load_images(self):
        """Load all chess piece images into memory."""
        piece_names = [
            "w_blt", "b_bdt", "w_nlt", "b_ndt",
            "w_klt", "b_kdt", "w_qlt", "b_qdt",
            "w_rlt", "b_rdt", "w_plt", "b_pdt"
        ]
        for piece in piece_names:
            filename = f"Chess_{piece[2:]}60.png"  # Use a consistent naming pattern
            image_path = self.images_dir / filename
            if image_path.exists():
                self.pieces[piece] =Tk.PhotoImage(file=image_path)
            else:
                print(f"Warning: {filename} not found in {self.images_dir}")

    def get_image(self, piece_name):
        """Retrieve an image by piece name."""
        return self.pieces.get(piece_name)

# Usage
if __name__ == "__main__":
    root =Tk.Tk()
    

    # Set the directory where images are stored
    images_dir = r"E:\Games\pythonsid\python_chess\python_chess\pngs"
    chess_images = ChessImages(images_dir)
    chess_images.load_images()

    # Example: Access the black bishop image
    b_bishop_image = chess_images.get_image("b_bdt")
    print(f"Loaded b_bishop image: {b_bishop_image}")
    label=Tk.Label(image= b_bishop_image)
    label.pack()
    root.mainloop()


