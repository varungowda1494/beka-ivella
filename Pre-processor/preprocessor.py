from __future__ import unicode_literals

class cresource:
    def __init__(self, id, name, features):
        self.__id = id
        self.name = name
        self.features = features
    def getResourceID(self):
        print (self.__id)

import glob, os
import moviepy.editor as mp 

from retriever.retriever import getResource
from assigner.assigner import assignID
from mel_gen.mel import generate_features


def preprocess(resource, resource_type):

	#Aud_extractor and Retriever
	if(resource_type == "link"):
		getResource(resource,{'format': 'bestaudio/best', 
			'outtmpl': 'current',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'wav',
				'preferredquality': '192',
			}]})
	else:
		clip = mp.VideoFileClip(resource) 
		clip.audio.write_audiofile(resource)
	
	#	for file in os.listdir(""):
	#		if file.endswith(".txt"):
	#		    print(os.path.join("/mydir", file)) 
	
	if(glob.glob('wav')):
		a_files = glob.glob('wav')
		print(a_files)
	filename = "wav"

	#test = res.name
	feats = generate_features(filename)

	res = cresource(100, filename, feats)
	#print(generate_features(filename) == generate_features(test))

	return res

print(preprocess('https://www.youtube.com/watch?v=bEUupEmWcvk', "link").features)

