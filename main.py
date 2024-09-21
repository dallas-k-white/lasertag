import tkinter as tk
from tkinter import ttk
import splashScreen
import PlayerEdit

def root_builder() -> tk.Tk:
    root: tk.Tk = tk.Tk()
    root.title("Photon - Team 13")
    root.configure(background="white")
    return root

def main() -> None:
    root: tk.Tk = root_builder()
    splash: splashScreen = splashScreen.build(root)
    root.after(3000, splash.destroy)
    root.after(3000, PlayerEdit.build, root)

    root.mainloop()

main()

