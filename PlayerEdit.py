import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Edit Player Screen")
root.geometry("600x600")

main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Tema labels
team1_label = tk.Label(main_frame, text="Red 1", font=("Arial", 14))
team1_label.grid(row=0, column=0, padx=10)

team2_label = tk.Label(main_frame, text="Green 2", font=("Arial", 14))
team2_label.grid(row=0, column=2, padx=10)


team1_entries = []
team2_entries = []


for i in range(20):
    player_label = tk.Label(main_frame, text=f"Player {i+1}")
    player_label.grid(row=i+1, column=1, padx=10, pady=5)
    
    # Team1
    team1_entry = ttk.Entry(main_frame, width=20)
    team1_entry.grid(row=i+1, column=0, padx=10, pady=5)
    team1_entries.append(team1_entry)
    
    # Team2
    team2_entry = ttk.Entry(main_frame, width=20)
    team2_entry.grid(row=i+1, column=2, padx=10, pady=5)
    team2_entries.append(team2_entry)


root.mainloop()
