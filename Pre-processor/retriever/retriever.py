from __future__ import unicode_literals
import youtube_dl

def getResource(URI, opts={}):
	ydl_opts = opts
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([URI])


#getResource('https://www.youtube.com/watch?v=BaW_jenozKc',{'format': 'bestaudio/best',
#    'postprocessors': [{
#        'key': 'FFmpegExtractAudio',
#        'preferredcodec': 'wav',
#        'preferredquality': '192',
#    }]})
