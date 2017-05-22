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
gpio.setup(17,gpio.IN)
gpio.setup(27,gpio.IN)

def mpcmdr(p,cmd):
  print(cmd+'\n')
  while 1:
    l=p.stdout.readline()
    if not l:
      break
    #pass
  print(l+'\n')
  p.stdin.write(cmd+'\n')
  p.stdin.flush()
  return p.stdout.readline()

def mpcmd(p,cmd):
  print(cmd+'\n')
  p.stdin.write(cmd+'\n')
  p.stdin.flush()

path=os.environ["FRR_HOME"]+'/'+os.environ["FRR_CONF"]
# lecture sur la carte audio USB
# p=subprocess.Popen(['mplayer', '-ao', 'alsa:device=hw=1.0', '-slave', '-quiet', '-vo', 'sdl', path+'/media/metronome.mp4'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
p=subprocess.Popen(['mplayer', '-slave', '-quiet', '-vo', 'sdl', path+'/media/metronome.mp4'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
with open(path+'/playliste1.csv','r') as play:
  c = csv.reader(play,delimiter=',')
  for l in c:
    if l[0]!='nom du fichier': 
      mpcmd(p,'loadfile '+ path+'/media/'+l[0])

      #mode boucle
      if gpio.input(17)==1:
        mpcmd(p,'loop 0')
        time.sleep(1)
        while gpio.input(17)==1:
          time.sleep(1)
        mpcmd(p,'loop -1')

      #mode debug lecture pendant 10s max
      if gpio.input(27)==1:
        for i in range(100):
          time.sleep(0.1)
          if gpio.input(18)==1:
            p.kill()
            subprocess.call(["pkill","fbi"])
            subprocess.call(["halt"])
            exit()

      #mode duree fixe
      if (gpio.input(17)==0) and (gpio.input(27)==0):
        for i in range(int(l[2])*10):
          time.sleep(0.1)
          if gpio.input(18)==1:
            time.sleep(0.05)
            while gpio.input(18)==1:
              time.sleep(0.1)
            break

mpcmd(p,'quit')
exit()
