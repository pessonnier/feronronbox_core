# rien
print("lecture des videos")

import csv
import subprocess
import os
import time
import RPi.GPIO as gpio

os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_NOMOUSE', '1')

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.IN)

def mpcmd(p,cmd):
  print(cmd+'\n')
  p.stdin.write(cmd+'\n')
  p.stdin.flush()

path=os.environ["FRR_HOME"]+'/'+os.environ["FRR_CONF"]
p=subprocess.Popen(['mplayer', '-slave', '-quiet', '-vo', 'sdl', path+'/media/metronome.mp4'],stdin=subprocess.PIPE, universal_newlines=True)
with open(path+'/playliste1.csv','r') as play:
  c = csv.reader(play,delimiter=',')
  for l in c:
    if l[0]!='nom du fichier': 
      mpcmd(p,'loadfile '+ path+'/media/'+l[0])
      while gpio.input(18)==1:
        pass
      for i in range(100):
        time.sleep(0.1)
        if gpio.input(18)==1:
          break
      #mpcmd(p,'pause')
      #time.sleep(1)      
      #mpcmd(p,'pause')
      #p.wait()
mpcmd(p,'quit')
exit()
