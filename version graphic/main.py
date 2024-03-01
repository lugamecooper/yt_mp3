from pytubefix import YouTube,Playlist
from pytubefix.cli import on_progress
from re import findall

import tkinter
class main:
    def __init__(self) -> None:
        self.fen = tkinter.Tk("converisseur")
        self.fen.geometry(f"{self.fen.winfo_screenwidth()}x{self.fen.winfo_screenheight()}")
        self.fen.state("zoomed")
        self.div_input = tkinter.Frame(self.fen)
        self.div_input.pack()
        self.div_input.place(width="100px",height="400px")
        self.label_inp = tkinter.Label(self.div_input,text="vidéo à télécharger")
        self.label_inp.pack()
        self.fen.mainloop()

    def verify(self) -> str:
        from os.path import exists,dirname
        test_2 = findall(r"^(\w:\\Users\\[\w| ]*\\)",__file__)
        if len(test_2) == 1:
            test = exists(test_2[0]+"/Music")
        if not test:
            path = dirname(__file__)
        else:
            path = test_2[0]+"/Music"
        del exists,dirname
        return path
    
main()