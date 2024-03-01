from pytubefix import YouTube,Playlist
from pytubefix.cli import on_progress
from time import sleep
from os import system
from re import findall
from colorama import Fore

class main:
    def __init__(self) -> None:
        self.paht = self.verify()
        ping = system("ping youtube.com")# check the connection with youtube.com
        system("cls")
        if ping:
            print("votre pc n'est pas connecter à internet ou le site de youtube est hors ligne\n",
                  "you're compupter is not connected to internet or youtube is down")
            input()
            exit()
        while True:
            self.type_téléchargement = input("music [1] || video [0]\nmusique [1] || vidéo [0] : ")
            try:
                bool(int(self.type_téléchargement))
                self.type_téléchargement = bool(int(self.type_téléchargement))
                break
            except:
                print("vous n'avez pas saisi la bonne valeur\n",
                      "you have not entered the correct value")
                sleep(2)
                system("cls")
        while True:
            self.url = input("url : ")
            if "playlist" in self.url:
                self.téléchargement_playlist()
            else:
                self.téléchargement_video()

    def téléchargement_playlist(self):
        error = False
        try:
            playlist = Playlist(self.url)
        except Exception as er:
            print(er)
            print("l'url donnée n'est pas valide ou correct\n",
                  "the given url is not correct")
            return None
        for video in playlist.videos:
            if video.age_restricted:
                print(f"la vidéo {video.title} est soumise à une limite d'âge\n",
                      f"the video {video.title} is subject to an age limit")
            else:
                try:
                    title = video.title
                    title = title.replace("\n","")
                    title = title.replace("\\","")
                    title = title.replace("/","")
                    video.title = title
                except:
                    print("une erreur est survenue, elle vient de la librairie merci de recomancer.\n",
                          "an error has occurred, it comes from the library thank you for starting again.")
                    return None
                try:
                    if self.type_téléchargement:
                        video.streams.get_audio_only().download(self.paht,title,mp3=True)
                    else:
                        video.streams.get_highest_resolution().download(self.paht,title,mp3=False)
                    print(f"le téléchargement de {title} est fini\n",
                          f"the download of {title} is finished")
                except Exception as er:
                    print(er)
                    print(f"une erreur est survenue pour la vidéo {title}\n",
                          f"an error has occurred for the video {title}")
                    error = True
        if not error:
            system("cls")

    def téléchargement_video(self):
        error = False
        try:
            video = YouTube(self.url,on_progress_callback = on_progress)
        except Exception as er:
            print(er)
            print("l'url donnée n'est pas valide ou correct\n",
                  "the given url is not correct")
            return None
        if video.age_restricted:
            print(f"la vidéo {video.title} est soumise à une limite d'âge\n",
                  f"the video {video.title} is subject to an age limit")
            return None
        else:
            title = video.title
            title = title.replace("\n","")
            title = title.replace("\\","")
            title = title.replace("/","")
            try:
                if self.type_téléchargement:
                    video.streams.get_audio_only().download(self.paht,title,mp3=True)
                else:
                    video.streams.get_highest_resolution().download(self.paht,title,mp3=False)
            except Exception as er:
                print(er)
                print(f"une erreur est survenue pour la vidéo {title}\n",
                      f"an error has occurred for the video {title}")
                error = True
            if not error:
                system("cls")
                print(f"le téléchargement de {title} est fini\n",
                      f"the download of {title} is finished")

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