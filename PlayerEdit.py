import tkinter as tk
from tkinter import ttk
import udp_handler
import PlayerAction
from PIL import ImageTk, Image
from Database import find_player, add_player
import tkinter.simpledialog as simpledialog
udp_handler_instance = udp_handler.get_instance()

def check_player(codename_entry: tk.Entry, equipment_id_entry: tk.Entry, next_entry: tk.Entry):

    def check_func(event):
        equipment_id_entry.delete(0,tk.END)
        codename_entry.delete(0,tk.END)
        if(len(event.widget.get()) == 0):
            equipment_id_entry.config(state="disabled");
            codename_entry.config(state="disabled");
            return;

        codename = find_player(int(event.widget.get()))
        if codename:  # If a player is found
            codename_entry.config(state="enabled") #you can only edit a field if it is enabled 
            codename_entry.delete(0,tk.END)
            codename_entry.insert(0, codename)  # Insert the found codename
            codename_entry.config(state="disabled") 
        else:
            codename = simpledialog.askstring("Player Codename", "Please enter the player codename")
            if codename is None:
                return
            codename_entry.config(state="enabled") 
            codename_entry.insert(0, str(codename))  # Insert the found codename
        equipment_id = simpledialog.askinteger("Equipment ID", f"Enter equipment ID for {codename}:", minvalue=1)

        if(equipment_id is None or codename is None):
            equipment_id_entry.delete(0,tk.END)
            codename_entry.delete(0,tk.END)
            equipment_id_entry.config(state="disabled");
            codename_entry.config(state="disabled");
            return;

        equipment_id_entry.config(state="enabled")
        equipment_id_entry.insert(0,str(equipment_id));
        udp_handler_instance.transmit_equipment_id(equipment_id);
        if(next_entry is not None):
            next_entry.config(state="enabled") 
            next_entry.focus()
    return check_func;

def build(root: tk.Tk) -> None:
    root.title("Edit Player Screen")
    root.geometry("1200x700")

    main_frame = tk.Frame(root)

    #Buttons
    f12_clear_button = tk.Button(main_frame, text="F12\n Clear Entries", height = 3, command=lambda: clear_entries_f12())
    f12_clear_button.grid(row = 1, column=1, pady=100, sticky="n")
    f5_start_game = tk.Button(main_frame, text="F5\n Start Game", height = 3, command=lambda: switch_to_play_action())
    f5_start_game.grid(row = 1, column=1, pady=100, sticky="s")

    entry_label = tk.Label(main_frame, text="use Enter to check IDs", font=("Arial", 12))
    entry_label.grid(row=0,column=1,pady=5)
    main_frame.pack(expand=tk.YES,fill=tk.BOTH)
    #Team1
    team1_frame = tk.LabelFrame(main_frame, text="Red Team", font=("Arial", 12), fg="red")
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

    team1_next = None
    team2_next = None
    #Adding entries
    for i in reversed(range(20)):

        # Team 1
        team1_id_label = tk.LabelFrame(team1_frame, text="ID", font=("Arial", 10))
        team1_id_label.grid(row=i, column=0, sticky="w", padx=5)


        team1_player_label = tk.Label(team1_frame, text="Codename", font=("Arial", 10))
        team1_player_label.grid(row=i, column=2, sticky="w", padx=5)

        team1_entry = ttk.Entry(team1_frame, width=15, state="disabled")
        team1_entry.grid(row=i, column=3, padx=5, pady=2, sticky="w")
        team1_entries.append(team1_entry)

        team1_equipment_label = tk.Label(team1_frame, text="Equipment ID", font=("Arial", 10))
        team1_equipment_label.grid(row=i, column=4, sticky="w", padx=5)

        team1_equipment = ttk.Entry(team1_frame, width=6, state="disabled")
        team1_equipment.grid(row=i, column=5, padx=5, pady=2, sticky="w")
        team1_equipment_ids.append(team1_equipment)

        team1_id = ttk.Entry(team1_frame, width=4)
        team1_id.bind("<Return>",check_player(team1_entry,team1_equipment,team1_next));
        team1_id.grid(row=i, column=1, padx=5, pady=2, sticky="w")
        team1_ids.append(team1_id)
        if(i != 0):
            team1_id.config(state="disabled")
        team1_next = team1_id;

        # Team 2
        team2_id_label = tk.Label(team2_frame, text="ID", font=("Arial", 10))
        team2_id_label.grid(row=i, column=0, sticky="w", padx=5)

        team2_id = ttk.Entry(team2_frame, width=4)
        team2_id.grid(row=i, column=1, padx=5, pady=2, sticky="w")
        team2_ids.append(team2_id)

        team2_player_label = tk.Label(team2_frame, text="Codename", font=("Arial", 10))
        team2_player_label.grid(row=i, column=2, sticky="w", padx=5)

        team2_entry = ttk.Entry(team2_frame, width=15,state="disabled")
        team2_entry.grid(row=i, column=3, padx=5, pady=2, sticky="w")
        team2_entries.append(team2_entry)

        team2_equipment_label = tk.Label(team2_frame, text="Equipment ID", font=("Arial", 10))
        team2_equipment_label.grid(row=i, column=4, sticky="w", padx=5)

        team2_equipment = ttk.Entry(team2_frame, width=6, state="disabled")
        team2_equipment.grid(row=i, column=5, padx=5, pady=2, sticky="w")
        team2_equipment_ids.append(team2_equipment)
        team2_id.bind("<Return>",check_player(team2_entry,team2_equipment,team2_next));
        team2_id.bind("<Tab>",check_player(team2_entry,team2_equipment,team2_next));
        if(i != 0):
            team2_id.config(state="disabled")
        team2_next = team2_id;


    def clear_entries_f12():
        for i in range(20):
            team1_ids[i].delete("0", "end")
            if i != 19:
                team1_ids[i].config(state="disabled")
            team1_entries[i].config(state="enabled")
            team1_entries[i].delete("0", "end")
            team1_entries[i].config(state="disabled")
            team1_equipment_ids[i].delete("0","end")
            team1_equipment_ids[i].config(state="disabled")

            team2_ids[i].delete("0", "end")
            if i != 19:
                team2_ids[i].config(state="disabled")
            team2_entries[i].config(state="enabled")
            team2_entries[i].delete("0", "end")
            team2_entries[i].config(state="disabled")
            team2_equipment_ids[i].delete("0","end")
            team2_equipment_ids[i].config(state="disabled")
    
    def switch_to_play_action():
        teams = check_all_players()
        if not teams:
            return; 
        root.unbind("<F12>")
        root.unbind("<F5>")
        main_frame.destroy()
        background_img = Image.open("images/background.tif")
        background = ImageTk.PhotoImage(background_img)
        background_label = tk.Label(root, image=background)
        background_label.image = background
        background_label.place(relwidth=1, relheight=1)


        alert_img = Image.open("images/alert.tif")
        alert = ImageTk.PhotoImage(alert_img)
        alert_label = tk.Label(root, image=alert, bd=0, highlightthickness=0)
        alert_label.image = alert
        alert_label.place(relwidth=1)


        def countdown(i):
            if i >= 0:
                second_imgs = Image.open(f"images/{i}.tif")
                second = ImageTk.PhotoImage(second_imgs)

                seconds_label = tk.Label(root, image=second)
                seconds_label.image = second
                seconds_label.place(relx=0.5, rely=0.55, anchor="center")

                root.after(1000, lambda: (seconds_label.destroy(), countdown(i - 1)))
            else:
                root.after(1, alert_label.destroy(), background_label.destroy())
                root.after(1, PlayerAction.get_player_action(teams[0],teams[1]), root)
        
        root.after(1000, countdown, 30)

        


    def check_all_players():
        team1_players = []
        team2_players = []
        for i in range(20):
            team1_id_value = team1_ids[i].get()
            if team1_id_value: 
                try:
                    player1_codename = find_player(int(team1_id_value))
                    if player1_codename: 
                        team1_entries[i].delete(0, tk.END)
                        team1_entries[i].insert(0, player1_codename)
                    else:
                        player1_codename = team1_entries[i].get().strip()
                        if team1_entries[i].get is None or len(team1_entries[i].get().strip()) == 0: 
                            simpledialog.messagebox.showerror("invalid codename",f"invalid Codename for {team1_id_value}");
                            return None 
                        add_player(team1_entries[i].get().strip(), int(team1_id_value))

                    equipment_id = team1_equipment_ids[i].get();
                    if len(equipment_id) == 0:
                        simpledialog.messagebox.showerror("invalid equipment id",f"invalid Equipment ID for {team1_id_value}");
                        return None 
                    udp_handler_instance.transmit_equipment_id(equipment_id) 
                    team1_players.append((team1_id_value,player1_codename,equipment_id))
                except ValueError:
                    return None

            team2_id_value = team2_ids[i].get()
            if team2_id_value: 
                try:
                    player2_codename = find_player(int(team2_id_value))
                    if player2_codename: 
                        team2_entries[i].delete(0, tk.END)
                        team2_entries[i].insert(0, player2_codename)
                    else:
                        player2_codename = team2_entries[i].get().strip()
                        if team2_entries[i].get() is None or len(team2_entries[i].get().strip()) == 0: 
                            simpledialog.messagebox.showerror("invalid codename",f"invalid Codename for {team2_id_value}");
                            return None 
                        add_player(team2_entries[i].get().strip(), int(team2_id_value))

                    equipment_id = team2_equipment_ids[i].get();
                    if len(equipment_id) == 0:
                        simpledialog.messagebox.showerror("invalid equipment id",f"invalid Equipment ID for {team2_id_value}");
                        return None 
                        udp_handler_instance.transmit_equipment_id(equipment_id) 
                    team2_players.append((team2_id_value,player2_codename,equipment_id))
                except ValueError:
                    return None                
        return (team1_players,team2_players)            
            
    root.bind('<F12>', lambda event: clear_entries_f12())
    root.bind('<F5>', lambda event: switch_to_play_action())
