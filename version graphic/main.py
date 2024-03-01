from pytubefix import YouTube,Playlist
from pytubefix.cli import on_progress
from re import findall

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