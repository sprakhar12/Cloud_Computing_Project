#!usr/bin/env python
from __future__ import print_function
import json
import os
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    username='7b5c3f47-9545-46fc-a4ef-1d421d727b31',
    password='MR7DViObD3IW',
    version='2017-09-26')

#KodK0d122017.

#print("tone_chat() example 1:\n")
#utterances = [{'text': '"More that all @HerdFB away games and half' + 'their of their \n '
#'home games. Oh its True ... '
#'Damn True! #IamBecauseWeAre https://t.co/GZ1qHgixNK"', 'user': 'herdHater'},{'text': 'It is a good day.', 'user': 'glenn'},{'text': 'I am very happy. It is a good day.', 'user': 'hande'}]
#print(json.dumps(tone_analyzer.tone_chat(utterances), indent=2))

directory = './resources/'
OutFile = ''
print("hi")
print("Analyzing all files in " + directory)
for fn in os.listdir(directory):
	print("File " + fn + " " +fn[len(fn)-4:len(fn)])
	if fn[len(fn)-4:len(fn)] == 'json':
		OutFile = directory +fn[0:len(fn)-4]+'_ans.json'
		print("working on file"+fn)
		#with open(join(dirname(__file__),'./resources/tone.json')) as tone_json:
		# tone = tone_analyzer.tone(json.load(tone_json)['text'], "text/plain")
		with open(os.path.join(directory, fn), 'r') as jsonfile:
		   tone = tone_analyzer.tone(json.load(jsonfile),content_type='application/json')
		#print(json.dumps(tone, indent=1))
		write_json( tone, OutFile)


def write_json( data, out_file):
    print("Writing"+out_file)	
    with open(out_file, "w") as f:
        f.write(json.dumps(data))
