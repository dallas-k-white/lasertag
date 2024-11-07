import tkinter as tk
from tkinter import ttk
from Database import get_players, find_player
import udp_handler 

def get_player_action(team1_entered_players, team2_entered_players):

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

        team1_players = [p[1] for p in team1_entered_players]

        team1_listbox = tk.Listbox(team1_frame, selectmode=tk.SINGLE, height=10, exportselection=0)
        team1_listbox.grid(row=1, column=0, padx=10, pady=5)
        for player in team1_players:
            team1_listbox.insert(tk.END, player)

        # Green team
        team2_frame = tk.LabelFrame(main_frame, text="Green Team", font=("Arial", 12), labelanchor="n", fg="green")
        team2_frame.grid(row=1, column=2, padx=10, pady=2, sticky="n")

        team2_players = [p[1] for p in team2_entered_players]


        team2_listbox = tk.Listbox(team2_frame, selectmode=tk.SINGLE, height=10, exportselection=0)
        team2_listbox.grid(row=1, column=0, padx=10, pady=5)
        for player in team2_players:
            team2_listbox.insert(tk.END, player)


        log_label = tk.Label(action_log_frame, text="Action Log", font=("Arial", 12))
        log_label.grid(row=0, column=0)

        log_listbox = tk.Listbox(action_log_frame, width=50, height=20)
        log_listbox.grid(row=1, column=0, padx=10, pady=10)

        #play_track()

        # For testing purposes
        action_frame = tk.Frame(main_frame)
        action_frame.grid(row=1, column=1, padx=10)
    
    return build_player_action

# def play_track():
#     tracks = ["Tracks/Track01.mp3", "Tracks/Track02.mp3", "Tracks/Track03.mp3", "Tracks/Track04.mp3", "Tracks/Track05.mp3",
#               "Tracks/Track06.mp3", "Tracks/Track07.mp3", "Tracks/Track08.mp3"]
#     t = random.choice(tracks)
#     pygame.mixer.music.load(t)
#     print(t)
#     pygame.mixer.music.play(loops=0)



if __name__ == "__main__":
    root = tk.Tk()
    get_player_action([(1,"player 1",1),(2,"player 2",2)],[(3,"player 3",3),(4,"player 4",4)])(root)
    play_track()
    root.mainloop()
