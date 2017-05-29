# lecture en boucle des videos
# IHM à boutons
print("lecture des videos")

import csv
import subprocess
import os
import time
import RPi.GPIO as gpio

# lire une variable avec le peripherique audio et video
path=os.environ["FRR_HOME"]+'/'+os.environ["FRR_CONF"]
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_NOMOUSE', '1')

gpio.setmode(gpio.BCM)
gpio.setup(18,gpio.IN) # btt vert
gpio.setup(17,gpio.IN) # droite
gpio.setup(27,gpio.IN) # gauche

PAUSE=0.2

def mpcmdr(p,cmd):
  print(cmd+'\n')
  p.stdin.write(cmd+'\n')
  p.stdin.flush()
  while 1:
    l=p.stdout.readline()
    if l.startswith('ANS'):
      break
  print(l+'\n')
  return l.split('=')[1].strip(' \'')

def mpcmd(p,cmd):
  print(cmd+'\n')
  p.stdin.write(cmd+'\n')
  p.stdin.flush()

loop=False

def modeBoucle():
  global loop
  if gpio.input(17)==1:
    if not loop:
      mpcmd(p,'loop 10')
      loop=True
    time.sleep(1)
    while gpio.input(17)==1:
      time.sleep(0.1)
      if gpio.input(18)==1:
        break # passe à la video suivante
    mpcmd(p,'loop -1')
    loop=False

while 1:
  # lecture sur la carte audio USB
  # p=subprocess.Popen(['mplayer', '-ao', 'alsa:device=hw=1.0', '-slave', '-quiet', '-idle', '-vo', 'sdl', path+'/media/metronome.mp4'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
  p=subprocess.Popen(['mplayer', '-slave', '-quiet', '-idle', '-vo', 'sdl', path+'/media/metronome.mp4'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
  with open(path+'/playliste1.csv','r') as play:
    c = csv.reader(play,delimiter=',')
    for l in c:
      if l[0]!='nom du fichier':
        if p.poll()==None:
          mpcmd(p,'loadfile '+ path+'/media/'+l[0])
        else:
          p=subprocess.Popen(['mplayer', '-slave', '-quiet', '-idle', '-vo', 'sdl', path+'/media/'+l[0]],stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)

        modeBoucle()

        # mode debug lecture pendant 10s max
        if gpio.input(27)==1:
          for i in range(int(10/PAUSE)):
            time.sleep(PAUSE)
            if gpio.input(18)==1: # arreter le pi
              p.kill()
              subprocess.call(["sudo", "pkill", "fbi"])
              time.sleep(1)
              subprocess.call(["sudo", "halt"])
              exit()

        # mode lecture normale
        if (gpio.input(17)==0) and (gpio.input(27)==0):
          duree=int(l[2])
          for i in range(int(duree/PAUSE)):
            time.sleep(PAUSE)
            if gpio.input(18)==1:
              time.sleep(0.05)
              while gpio.input(18)==1:
                time.sleep(PAUSE)
              break # passe à la video suivante
            if gpio.input(17)==1: # passer en mode boucle
              if not loop:
                mpcmd(p,'loop 10')
                loop=True
                break
        
        modeBoucle() # rentrer dans le mode boucle si l'on sort mode normal en basculant à droite
              
  mpcmd(p,'quit')
exit()
