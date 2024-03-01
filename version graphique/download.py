from pytubefix import YouTube,Playlist
from pytubefix.cli import on_progress
from time import sleep
from os import system
from re import findall
from colorama import Fore

class main:
    def __init__(self) -> None:
        pass
        
    def download(self,url,Type_output,type_input,path) -> tuple[int,str|list]:
        if url == "":
            return (1,"url vide")
        self.path = path
        ping = system("ping youtube.com")# check the connection with youtube.com
        if ping:
            return (1,"votre pc n'est pas connecter à internet ou le site de youtube est hors ligne",)
        self.type_téléchargement = Type_output
        while True:
            self.url = url
            if type_input:
                return self.téléchargement_playlist()
            else:
                return self.téléchargement_video()

    def téléchargement_playlist(self):
        try:
            playlist = Playlist(self.url)
        except Exception as er:
            return (1,"l'url donnée n'est pas valide ou correct",)
        list_video = []
        for video in playlist.videos:
            if video.age_restricted:
                list_video.append(f"la vidéo {video.title} est soumise à une limite d'âge")
            else:
                try:
                    title = video.title
                    title = title.replace("\n","")
                    title = title.replace("\\","")
                    title = title.replace("/","")
                    video.title = title
                except:
                    list_video.append(None)
                try:
                    if self.type_téléchargement:
                        video.streams.get_audio_only().download(self.path,title,mp3=True)
                    else:
                        video.streams.get_highest_resolution().download(self.path,f"{title}.mp4",mp3=False)
                    list_video.append(f"le téléchargement de {title} est fini")
                except Exception as er:
                    list_video.append(f"une erreur est survenue pour la vidéo {title}")
            return (0,list_video,)

    def téléchargement_video(self):
        error = False
        try:
            video = YouTube(self.url,on_progress_callback = on_progress)
        except Exception as er:
            return (1,"l'url donnée n'est pas valide ou correct",)
        if video.age_restricted:
            return (0,[f"la vidéo {video.title} est soumise à une limite d'âge"],)
        else:
            title = video.title
            title = title.replace("\n","")
            title = title.replace("\\","")
            title = title.replace("/","")
            try:
                if self.type_téléchargement:
                    video.streams.get_audio_only().download(self.path,title,mp3=True)
                else:
                    video.streams.get_highest_resolution().download(self.path,f"{title}.mp4",mp3=False)
            except Exception as er:
                return (0,[f"une erreur est survenue pour la vidéo {title}"],)
            return (0,[f"le téléchargement de {title} est fini"],)