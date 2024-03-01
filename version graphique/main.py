from pytubefix import YouTube,Playlist
from pytubefix.cli import on_progress
from re import findall
import download
import tkinter
class main:
    def __init__(self) -> None:
        self.fen = tkinter.Tk("converisseur")
        self.fen.geometry(f"{self.fen.winfo_screenwidth()}x{self.fen.winfo_screenheight()}")
        self.fen.state("zoomed")
        self.div_général = tkinter.Frame(self.fen)
        self.div_général.pack(anchor="w")
        self.div_input = tkinter.Frame(self.div_général)
        self.div_input_2 = tkinter.Frame(self.div_général)
        self.label_inp = tkinter.Label(self.div_input,text="vidéo à télécharger : ")
        self.inp = tkinter.Entry(self.div_input)
        self.label_blank = tkinter.Label(self.div_input_2,text="                      ")
        self.button_inp = tkinter.Button(self.div_input_2,text="télécharger",borderwidth=5)
        self.div_général.pack()
        self.label_inp.pack(side="left")
        self.label_blank.pack(side="left")
        self.inp.pack(side="right")
        self.button_inp.pack(side="right")
        self.div_input.pack()
        self.div_input_2.pack()

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
    
    def lunch_download(self):
        url = self.inp.get()
        state = download.main().download(url)
        

main()