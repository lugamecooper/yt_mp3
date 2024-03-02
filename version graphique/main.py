from pytubefix import YouTube,Playlist
from pytubefix.cli import on_progress
from re import findall
import download
import tkinter
from tkinter import filedialog

class main:
    def __init__(self) -> None:
        self.path = self.verify()

        self.fen = tkinter.Tk("yt_mp3",className="youtube mp3")
        self.fen.geometry(f"{self.fen.winfo_screenwidth()}x{self.fen.winfo_screenheight()}")
        self.fen.state("zoomed")
        self.div_général = tkinter.Frame(self.fen)
        self.div_général.pack(anchor="w")
        self.div_input = tkinter.Frame(self.div_général)
        self.div_input_2 = tkinter.Frame(self.div_général)
        self.label_inp = tkinter.Label(self.div_input,text="vidéo à télécharger : ")
        self.inp = tkinter.Entry(self.div_input)
        self.label_blank = tkinter.Label(self.div_input_2,text="                      ")
        self.button_inp = tkinter.Button(self.div_input_2,text="télécharger",borderwidth=5,command=self.lunch_download)

        self.label_error = tkinter.Label(self.div_général,text="")
        self.select_folder = tkinter.Button(self.div_général,text=f"changer de dossier\nactuelle : '{self.path}'",command=self.select_directory)

        self.frame_radio = tkinter.Frame(self.div_général)

        self.extansion_sorti = tkinter.IntVar(self.frame_radio,value=True)
        self.radio_1 = tkinter.Radiobutton(self.frame_radio,variable=self.extansion_sorti,value=True,indicatoron=0,text="musique")
        self.radio_2 = tkinter.Radiobutton(self.frame_radio,variable=self.extansion_sorti,value=False,indicatoron=0,text="vidéo")

        self.type_entree = tkinter.IntVar(self.frame_radio,value=False)
        self.radio_3 = tkinter.Radiobutton(self.frame_radio,variable=self.type_entree,value=True,indicatoron=0,text="playlist")
        self.radio_4 = tkinter.Radiobutton(self.frame_radio,variable=self.type_entree,value=False,indicatoron=0,text="vidéo")

        self.radio_black = tkinter.Label(self.frame_radio,text="      ")

        self.div = tkinter.Frame(self.fen)
        self.listbox = tkinter.Listbox(self.div)
        scrollbar = tkinter.Scrollbar(self.div)
        self.listbox.config(yscrollcommand=scrollbar.set,height=self.fen.winfo_screenheight(),width=125)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side=tkinter.RIGHT)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.div.pack(side=tkinter.RIGHT)


        self.div_général.pack()
        self.label_inp.pack(side="left")
        self.label_blank.pack(side="left")
        self.inp.pack(side="right")
        self.button_inp.pack(side="right")
        self.div_input.pack()
        self.div_input_2.pack()
        self.label_error.pack()
        self.select_folder.pack()
        self.frame_radio.pack()
        self.radio_1.pack(side="left")
        self.radio_2.pack(side="left")
        self.radio_black.pack(side="left")
        self.radio_3.pack(side="right")
        self.radio_4.pack(side="right")

        self.fen.mainloop()

    def verify(self) -> str:
        test = False
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
    
    def select_directory(self):
        test = filedialog.askdirectory(title="séléctionner le dossier cible", initialdir=self.path)
        if test:
            self.path = test
            self.select_folder.config(text=f"changer de dossier\nactuelle : '{self.path}'")
            self.select_folder.update()

    def lunch_download(self):
        url = self.inp.get()
        state = download.main().download(url,path=self.path, type_input=self.type_entree.get(), Type_output=self.extansion_sorti.get())
        if state[0]:
            self.label_error.config(text=state[1])
            self.label_error.update()
        else:
            self.listbox.delete(first=0,last=self.listbox.size()-1)
            for video in state[1]:
                self.listbox.insert(tkinter.END,video)
            self.listbox.update()

main()