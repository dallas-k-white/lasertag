import pygame
import random

def play_track():
        tracks = ["Tracks/Track01.mp3", "Tracks/Track02.mp3", "Tracks/Track03.mp3", "Tracks/Track04.mp3", "Tracks/Track05.mp3",
                "Tracks/Track06.mp3", "Tracks/Track07.mp3", "Tracks/Track08.mp3"]
        t = random.choice(tracks)
        pygame.mixer.music.load(t)
        print(t)
        pygame.mixer.music.play(loops=0)