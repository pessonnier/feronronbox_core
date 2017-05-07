import csv
import youtube_dl

print("téléchargement youtube")
with open('/home/pi/ferronron_squelette/liste_youtube.csv','r') as y:
  c = csv.reader(y,delimiter=',')
  for l in c[1:]:
    with youtube_dl.YoutubeDL({'outtmpl':"/home/pi/ferronron_squelette/media/"+l[0],'format':'best[height<=240]'}) as ydl:
      ydl.download(['http://www.youtube.com/watch?v='+l[1]])
