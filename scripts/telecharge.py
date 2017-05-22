print("téléchargement youtube")

import csv
import youtube_dl
import os

path=os.environ["FRR_HOME"]+'/'+os.environ["FRR_CONF"]
with open(path+'/liste_youtube.csv','r') as y:
  c = csv.reader(y,delimiter=',')
  for l in c:
    with youtube_dl.YoutubeDL({'outtmpl':path+'/media/'+l[0],'format':'best[height<=240]'}) as ydl:
      if l[1]!=' id': 
        ydl.download(['http://www.youtube.com/watch?v='+l[1]])
        #i=ydl.extract_info('http://www.youtube.com/watch?v='+l[1],download=False)
        #print(l[0]+' '+i.get('duration'))
