import os
import sys
from pygame import mixer


music_dir = "C:\\Users\\abc\\Desktop\\project work\\jarvis\\songs"
songs = os.listdir(music_dir)
os.startfile(os.path.join(music_dir, songs[0]))

    
# if sys.argv[1] == "play":
#     mixer.init()
#     mixer.music.load('C:/Users/abc/Desktop/project work/jarvis/songs/gallan kardi.mp3')
#     mixer.music.play()