import csv
import youtube_dl

with open('./ferronron_squelette/liste_youtube.csv','r') as y:
  c = csv.reader(y,delimiter=',')
  for l in c:
    with youtube_dl.YoutubeDL({'outtmpl':l[0],'format':'best[height<=240]'}) as ydl:
      ydl.download(['http://www.youtube.com/watch?v='+l[1][1:]])
