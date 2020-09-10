# based on http://dzone.com/snippets/set-windows-desktop-wallpaper
import win32api, win32con, win32gui
import glob
from random import randint
import os 
#----------------------------------------------------------------------
def setWallpaper(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, 1+2)
if __name__ == "__main__":
    directory = os.path.dirname(os.path.realpath(__file__))
    wallpapers = glob.glob("wallpapers/*")
    x = randint(0,len(wallpapers)-1)
    path = directory+"/" + wallpapers[x]
    # path = r'C:\Users\abc\Desktop\project work\jarvis\J.A.R.V.I.S-master\wallpapers\403880.jpg'
    setWallpaper(path)

# from gi.repository import Gio
# import glob
# from random import randint
# import os 


# directory = os.path.dirname(os.path.realpath(__file__))
# wallpapers = glob.glob("wallpapers/*")
# x = randint(0,len(wallpapers)-1)

# SCHEMA = 'org.gnome.desktop.background'
# KEY = 'picture-uri'
# gsettings = Gio.Settings.new(SCHEMA)
# background = directory+"/" + wallpapers[x]
# gsettings.set_string(KEY, "file://" + background)
