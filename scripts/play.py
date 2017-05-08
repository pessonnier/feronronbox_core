# rien
print("lecture des videos")

import csv
import subprocess
import os
import time

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_NOMOUSE', '1')

path=os.environ["FRR_HOME"]+'/'+os.environ["FRR_CONF"]
with open(path+'/playliste1.csv','r') as play:
  c = csv.reader(play,delimiter=',')
  for l in c:
    if l[0]!='nom du fichier': 
      p=subprocess.Popen(['mplayer', '-slave', '-quiet', '-vo', 'sdl', path+'/media/'+l[0]],stdin=subprocess.PIPE)
      time.sleep(5)
      print('cmd quit\n')
      p.stdin.write(b"quit\n")
      p.stdin.flush()
      p.wait()
