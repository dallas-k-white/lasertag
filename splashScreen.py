import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk


def hide_image(label):
    if label.winfo_exists():
        label.destroy()

def build(root: tk.Tk):

    def resize_image(event):
        if label.winfo_exists():
            new_width = event.width
            new_height = event.height
            image = img.resize((new_width, new_height))
            logo = ImageTk.PhotoImage(image)
            label.config(image=logo)
            label.image = logo

    root.title("Splash Screen")
    root.geometry("600x600")


    img = Image.open("logo.jpg")
    logo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=logo)
    label.pack(fill=tk.BOTH, expand=tk.YES)

    root.bind('<Configure>', resize_image)

    return label
    #root.after(3000, hide_image, label)
    #root.mainloop()
# splash_screen()