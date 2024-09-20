import tkinter as tk
from tkinter import ttk
from Database import find_player, add_player
 

root = tk.Tk()
root.title("Edit Player Screen")
root.geometry("850x700")

main_frame = tk.Frame(root)
main_frame.pack(pady=10, padx=10)

#Buttons
check_players_button = ttk.Button(main_frame, text="Check All Players", command=lambda: check_all_players())
check_players_button.grid(row=0, column=1, pady=5)

#Team1
team1_frame = tk.LabelFrame(main_frame, text="Red Team", font=("Arial", 12), labelanchor="n", fg="red")
team1_frame.grid(row=1, column=0, padx=10, pady=2, sticky="n")

team1_entries = []
team1_ids = []

#Team2
team2_frame = tk.LabelFrame(main_frame, text="Green Team", font=("Arial", 12), labelanchor="n", fg="green")
team2_frame.grid(row=1, column=2, padx=10, pady=2, sticky="n")

team2_entries = []
team2_ids = []

#Adding entries
for i in range(20):

    #Team1
    team1_id_label = tk.Label(team1_frame, text="ID", font=("Arial", 10))
    team1_id_label.grid(row=i, column=0, sticky="w", padx=5)

    team1_id = ttk.Entry(team1_frame, width=4)
    team1_id.grid(row=i, column=1, padx=5, pady=2, sticky="w")
    team1_ids.append(team1_id)

    team1_player_label = tk.Label(team1_frame, text="Codename", font=("Arial", 10))
    team1_player_label.grid(row=i, column=2, sticky="w", padx=5)

    team1_entry = ttk.Entry(team1_frame, width=15)
    team1_entry.grid(row=i, column=3, padx=5, pady=2, sticky="w")
    team1_entries.append(team1_entry)

    #Team2
    team2_id_label = tk.Label(team2_frame, text="ID", font=("Arial", 10))
    team2_id_label.grid(row=i, column=0, sticky="w", padx=5)

    team2_id = ttk.Entry(team2_frame, width=4)
    team2_id.grid(row=i, column=1, padx=5, pady=2, sticky="w")
    team2_ids.append(team2_id)

    team2_player_label = tk.Label(team2_frame, text="Codename", font=("Arial", 10))
    team2_player_label.grid(row=i, column=2, sticky="w", padx=5)

    team2_entry = ttk.Entry(team2_frame, width=15)
    team2_entry.grid(row=i, column=3, padx=5, pady=2, sticky="w")
    team2_entries.append(team2_entry)


def check_all_players():
    for i in range(20):
        team1_entries[i] = find_player(team1_ids[i].get())
        if team1_entries[i] is None:
            add_player(team1_entries[i], team1_ids[i])
        team2_entries[i] = find_player(team2_ids[i].get())
        if team2_entries[i] is None:
            add_player(team2_entries[i], team2_ids[i])

root.mainloop()