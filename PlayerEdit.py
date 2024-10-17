import tkinter as tk
from tkinter import ttk
import udp_handler
import PlayerAction
from PIL import ImageTk, Image
from Database import find_player, add_player
import tkinter.simpledialog as simpledialog

def build(root: tk.Tk) -> None:
    udp_handler_instance = udp_handler.get_instance()
    root.title("Edit Player Screen")
    root.geometry("1200x700")

    main_frame = tk.Frame(root)
    main_frame.pack(pady=10, padx=10)

    #Buttons
    check_players_button = ttk.Button(main_frame, text="Check All Players", command=lambda: check_all_players())
    check_players_button.grid(row=0, column=1, pady=5)
    f12_clear_button = tk.Button(main_frame, text="F12\n Clear Entries", height = 3, command=lambda: clear_entries_f12())
    f12_clear_button.grid(row = 1, column=1, pady=100, sticky="n")
    f5_start_game = tk.Button(main_frame, text="F5\n Start Game", height = 3, command=lambda: switch_to_play_action())
    f5_start_game.grid(row = 1, column=1, pady=100, sticky="s")

    #Team1
    team1_frame = tk.LabelFrame(main_frame, text="Red Team", font=("Arial", 12), labelanchor="n", fg="red")
    team1_frame.grid(row=1, column=0, padx=10, pady=2, sticky="n")

    team1_entries = []
    team1_ids = []
    team1_equipment_ids = []

    #Team2
    team2_frame = tk.LabelFrame(main_frame, text="Green Team", font=("Arial", 12), labelanchor="n", fg="green")
    team2_frame.grid(row=1, column=2, padx=10, pady=2, sticky="n")

    team2_entries = []
    team2_ids = []
    team2_equipment_ids = []

    #Adding entries
    for i in range(20):

        # Team 1
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

        team1_equipment_label = tk.Label(team1_frame, text="Equipment ID", font=("Arial", 10))
        team1_equipment_label.grid(row=i, column=4, sticky="w", padx=5)

        team1_equipment = ttk.Entry(team1_frame, width=6)
        team1_equipment.grid(row=i, column=5, padx=5, pady=2, sticky="w")
        team1_equipment_ids.append(team1_equipment)

        # Team 2
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

        team2_equipment_label = tk.Label(team2_frame, text="Equipment ID", font=("Arial", 10))
        team2_equipment_label.grid(row=i, column=4, sticky="w", padx=5)

        team2_equipment = ttk.Entry(team2_frame, width=6)
        team2_equipment.grid(row=i, column=5, padx=5, pady=2, sticky="w")
        team2_equipment_ids.append(team2_equipment)


    def clear_entries_f12():
        for i in range(20):
            team1_ids[i].delete("0", "end")
            team1_entries[i].delete("0", "end")
            team1_equipment_ids = 0

            team2_ids[i].delete("0", "end")
            team2_entries[i].delete("0", "end")
            team2_equipment_ids = 0
    
    def switch_to_play_action():
        main_frame.destroy()

        background_img = Image.open("background.tif")
        background = ImageTk.PhotoImage(background_img)
        background_label = tk.Label(root, image=background)
        background_label.image = background
        background_label.place(relwidth=1, relheight=1)


        alert_img = Image.open("alert.tif")
        alert = ImageTk.PhotoImage(alert_img)
        alert_label = tk.Label(root, image=alert, bd=0, highlightthickness=0)
        alert_label.image = alert
        alert_label.place(relwidth=1)


        def countdown(i):
            if i >= 0:
                second_imgs = Image.open(f"{i}.tif")
                second = ImageTk.PhotoImage(second_imgs)

                seconds_label = tk.Label(root, image=second)
                seconds_label.image = second
                seconds_label.place(relx=0.5, rely=0.55, anchor="center")

                root.after(1000, lambda: (seconds_label.destroy(), countdown(i - 1)))
            else:
                root.after(1, alert_label.destroy(), background_label.destroy())
                root.after(1, PlayerAction.build_player_action, root)
        
        root.after(1000, countdown, 30)

        


    def check_all_players():
        for i in range(20):
        # Team 1
            team1_id_value = team1_ids[i].get()
            if team1_id_value:  # Ensure there is an ID to check
                try:
                    
                    player1_codename = find_player(int(team1_id_value))
                    if player1_codename:  # If a player is found
                        team1_entries[i].delete(0, tk.END)  # Clear current entry
                        team1_entries[i].insert(0, player1_codename)  # Insert the found codename

                        equipment_id = simpledialog.askinteger("Equipment ID", f"Enter equipment ID for {team1_entries[i].get()}:", minvalue=1)
                        udp_handler_instance.transmit_equipment_id(equipment_id)
                    else:
                        # If no player found, add the new player using the current entry
                        if team1_entries[i].get():  # Ensure there's something to add
                            add_player(team1_entries[i].get(), int(team1_id_value))

                            equipment_id = simpledialog.askinteger("Equipment ID", f"Enter equipment ID for {team1_entries[i].get()}:", minvalue=1)
                            udp_handler_instance.transmit_equipment_id(equipment_id)
                except ValueError:
                    print(f"Invalid ID entered for Team 1, index {i}")

            # Team 2
            team2_id_value = team2_ids[i].get()
            if team2_id_value:  # Ensure there is an ID to check
                try:
                    player2_codename = find_player(int(team2_id_value))
                    if player2_codename:
                        team2_entries[i].delete(0, tk.END)
                        team2_entries[i].insert(0, player2_codename)

                        equipment_id = simpledialog.askinteger("Equipment ID", f"Enter equipment ID for {team1_entries[i].get()}:", minvalue=1)
                        udp_handler_instance.transmit_equipment_id(equipment_id)
                    else:
                        if team2_entries[i].get():  # Ensure there's something to add
                            add_player(team2_entries[i].get(), int(team2_id_value))

                            equipment_id = simpledialog.askinteger("Equipment ID", f"Enter equipment ID for {team1_entries[i].get()}:", minvalue=1)
                            udp_handler_instance.transmit_equipment_id(equipment_id)
                except ValueError:
                    print(f"Invalid ID entered for Team 2, index {i}")

    root.bind('<F12>', lambda event: clear_entries_f12())
    root.bind('<F5>', lambda event: switch_to_play_action())
