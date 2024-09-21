import tkinter as tk
from PIL import ImageTk, Image
from tkinter import ttk

root = tk.Tk()

def hide_image(label):
    label.destroy()
    root.destroy()


def splash_screen():

    def resize_image(event):
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

    root.after(5000, hide_image, label)
    root.mainloop()
    
if __name__ == "__main__":
	splash_screen()
