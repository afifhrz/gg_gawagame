import tkinter as tk

class CardRoyaleGame():
    """
    This is controller class for the overall game for creating and maintaining
    the model and view classes in order to handle and facilitate communication
    between the model and view classes.
    """
    def __init__(self, master:tk.Tk, map_file:str) -> None:
        self._master = master
        self._master.title("Card Royale Game")
        # self.draw_banner()
        # self.farmModel = FarmModel(map_file=map_file)