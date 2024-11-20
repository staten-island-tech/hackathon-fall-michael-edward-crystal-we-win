import tkinter as tk
from tkinter import font
import json

class Game():
    def StartGame():
        pass

window = tk.Tk()
window.title("RHYTHM GAME")
window.geometry('800x500')
songs = []

with open('songs.json', 'r') as file:
    songs = json.load(file)

titlefont = font.Font(family='Times New Roman', size=100, weight='bold')
buttonfont = font.Font(family="Verdana", size=35, weight='bold')

class TitleScreen():
    def SongMenu(titlescreenstuff):
        for label in titlescreenstuff:
            label.destroy()
            
        songbuttons = []
        for song in songs:
            songbutton = tk.Button(window, text=song['name'], font=buttonfont, command=lambda: Game.StartGame())
            songbutton.pack()
            songbuttons.append(songbutton)
    
    def OpenScreen():
        titlescreenstuff = []
        title = tk.Label(window, text="Rhythm! game.", font=titlefont)
        title.pack()
        titlescreenstuff.append(title)
        
        startbutton = tk.Button(window, text='START GAME', font=buttonfont, command=lambda: TitleScreen.SongMenu(titlescreenstuff))
        startbutton.pack()
        titlescreenstuff.append(startbutton)
        
        
TitleScreen.OpenScreen()
window.mainloop()