import tkinter as tk
from tkinter import ttk
from Database import get_players, find_player
import udp_handler 

def build_player_action(root: tk.Tk) -> None:
    udp_handler_instance = udp_handler.get_instance()
    root.title("Player Action")
    root.geometry("1200x700")

    main_frame = tk.Frame(root)
    main_frame.pack(pady=10, padx=10)

    # Current player action
    action_log_frame = tk.Frame(main_frame)
    action_log_frame.grid(row=0, column=1, padx=10, pady=5)

    # Red team
    team1_frame = tk.LabelFrame(main_frame, text="Red Team", font=("Arial", 12), labelanchor="n", fg="red")
    team1_frame.grid(row=1, column=0, padx=10, pady=2, sticky="n")

    team1_players = ["Player 1", "Player 2", "Player 3", "Player 4"]  # Can delete after populate players is defined

    team1_listbox = tk.Listbox(team1_frame, selectmode=tk.SINGLE, height=10, exportselection=0)
    team1_listbox.grid(row=1, column=0, padx=10, pady=5)
    for player in team1_players:
        team1_listbox.insert(tk.END, player)

    # Green team
    team2_frame = tk.LabelFrame(main_frame, text="Green Team", font=("Arial", 12), labelanchor="n", fg="green")
    team2_frame.grid(row=1, column=2, padx=10, pady=2, sticky="n")

    team2_players = ["Player A", "Player B", "Player C", "Player D"]  # Can delete after populate players is defined

    team2_listbox = tk.Listbox(team2_frame, selectmode=tk.SINGLE, height=10, exportselection=0)
    team2_listbox.grid(row=1, column=0, padx=10, pady=5)
    for player in team2_players:
        team2_listbox.insert(tk.END, player)


    log_label = tk.Label(action_log_frame, text="Action Log", font=("Arial", 12))
    log_label.grid(row=0, column=0)

    log_listbox = tk.Listbox(action_log_frame, width=50, height=20)
    log_listbox.grid(row=1, column=0, padx=10, pady=10)

    # For testing purposes
    action_frame = tk.Frame(main_frame)
    action_frame.grid(row=1, column=1, padx=10)

   

    def populate_players():
        # Need to get working
        players = get_players()  # Get all players
        team1_players = []
        team2_players = []

        # Split players based off of even or odd
        # if ID even add to green team?
        #if ID odd add to red team?
        for p in players:
            if p[0] % 2 == 0:
                team1_players.append(p)
            elif p[0] % 2 == 1:
                team2_players.append(p)

        # Pt the players into their screen
        for player in team1_players:
            team1_listbox.insert(tk.END, player)

        for player in team2_players:
            team2_listbox.insert(tk.END, player)

    
    populate_players()

if __name__ == "__main__":
    root = tk.Tk()
    build_player_action(root)
    root.mainloop()
