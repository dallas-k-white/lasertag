import tkinter as tk
from tkinter import ttk
from Database import get_players, find_player
import PlayerEdit
import udp_handler 


def update_timer(label, remaining_time, disable_ui_func, return_button_frame, root):
    minutes, seconds = divmod(remaining_time, 60)
    time_str = f"{minutes:02}:{seconds:02}"
    label.config(text=time_str)

    if remaining_time <= 0:
        label.config(text="00:00")
        disable_ui_func(root)
        show_game_over(root)
        show_return_button(return_button_frame, root)
    else:
        label.after(1000, update_timer, label, remaining_time - 1, disable_ui_func, return_button_frame, root)

def disable_ui(root):
    for widget in root.winfo_children():

        if isinstance(widget, (tk.Button, tk.Entry, tk.Listbox)):
            widget.config(state=tk.DISABLED)

def show_return_button(return_button_frame, root):

    return_button = tk.Button(return_button_frame, text="Return to Player Edit Screen", font=("Arial", 14), command=lambda: go_to_player_edit_screen(root))
    return_button.pack(pady=10)

def go_to_player_edit_screen(root):

    for widget in root.winfo_children():
        widget.destroy()
        
    PlayerEdit.build(root)

def show_game_over(root):
    for widget in root.winfo_children():
        if widget.winfo_class() == 'Label' and widget.cget('text') == 'Game Over!':
            return
    
    game_over_label = tk.Label(root, text="Game Over!", font=("Arial", 30), fg="red", bg="black")
    game_over_label.place(relx=0.5, rely=0.6, anchor="center")

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

        # Timer Display
        timer_label = tk.Label(root, text="06:00", font=("Arial", 14), fg="black")
        timer_label.place(relx=0.95, rely=0.95, anchor='se')

        remaining_time = 6 * 60

        return_button_frame = tk.Frame(root)
        update_timer(timer_label, remaining_time, disable_ui, return_button_frame, root)

        return_button_frame.place(relx=0.5, rely=0.90, anchor='center')

        #play_track()

        # For testing purposes
        action_frame = tk.Frame(main_frame)
        action_frame.grid(row=1, column=1, padx=10)
    
    return build_player_action


if __name__ == "__main__":
    root = tk.Tk()
    get_player_action([(1,"player 1",1),(2,"player 2",2)],[(3,"player 3",3),(4,"player 4",4)])(root)
    root.mainloop()
