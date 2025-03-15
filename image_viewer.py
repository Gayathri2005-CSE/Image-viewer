import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")

        self.image_label = tk.Label(root)
        self.image_label.pack(expand=True)

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.prev_btn = tk.Button(self.btn_frame, text="<< Previous", command=self.prev_image)
        self.prev_btn.grid(row=0, column=0, padx=10)

        self.open_btn = tk.Button(self.btn_frame, text="Open Folder", command=self.load_images)
        self.open_btn.grid(row=0, column=1, padx=10)

        self.next_btn = tk.Button(self.btn_frame, text="Next >>", command=self.next_image)
        self.next_btn.grid(row=0, column=2, padx=10)

        self.image_list = []
        self.current_index = 0

    def load_images(self):
        folder = filedialog.askdirectory()
        if folder:
            self.image_list = [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(("png", "jpg", "jpeg", "gif", "bmp"))]
            self.current_index = 0
            self.show_image()

    def show_image(self):
        if self.image_list:
            image_path = self.image_list[self.current_index]
            image = Image.open(image_path)
            image = image.resize((600, 400), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.img)

    def next_image(self):
        if self.image_list and self.current_index < len(self.image_list) - 1:
            self.current_index += 1
            self.show_image()

    def prev_image(self):
        if self.image_list and self.current_index > 0:
            self.current_index -= 1
            self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    viewer = ImageViewer(root)
    root.mainloop()
