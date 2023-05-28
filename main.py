import tkinter as tk
from controller import Game

def play_game(root, map_file):
    main_root = Game.CardRoyaleGame(root, map_file=map_file)
    root.mainloop()

def main() -> None:
    """
    Build the root tk.TK instance, then call the play_game function and the path of 
    any choosen map file.
    """
    root = tk.Tk()
    map = "maps/map1.txt"
    play_game(root=root, map_file=map)

if __name__ == '__main__':
    main()