import tkinter as tk 
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("TicTacToe")
        self.mode = None
        self.currentplayer = "X"
        self.buttons = [[None for i in range(3)] for j in range(3)]
        self.create_mode_selection()
        def create_mode_selection(self):
            self.mode_frame = tk.Frame(self.window)
            self.mode_frame.pack()
            mode = tk.Label(self.mode_frame, text = "Select game mode")
            mode.pack()
            single_button = tk.Button(self.button, text = " Single Player ", command = lambda:
                      self.start_game("single"))
            single_button.pack()
            multi_button = tk.Button(self.button, text = " Multiplayer ", command = lambda:
                      self.start_game("multiplayer"))
            multi_button.pack()
            
if __name__ == "__main__":
    window = tk.Tk()
    game = TicTacToe(window)
    window.mainloop()

