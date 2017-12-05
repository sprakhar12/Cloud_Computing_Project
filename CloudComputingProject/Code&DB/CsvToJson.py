#!/usr/bin/python
##http://www.idiotinside.com/2015/09/18/csv-json-pretty-print-python/
##https://github.com/EricZaporzan/tone-analyzer/blob/master/tone_analyze.py

import sys, getopt
import csv
import json
import os

#Get Command Line Arguments
def main():
    input_file = ''
    output_file = ''
    format = 'pretty'
    read_csv( format)

#Read CSV File
def read_csv( format):
    csv_rows = []
    directory = './resources/'
    print("Analyzing all files in " + directory)
    for fn in os.listdir(directory):
	if fn[len(fn)-3:len(fn)] == 'csv':
		json_file =  directory +fn[0:len(fn)-4]+'.json'
		print("Working on file: " + os.path.join(directory, fn) + " "+json_file)
		with open(os.path.join(directory, fn), 'r') as csvfile:
			reader = csv.DictReader(csvfile)
			title = reader.fieldnames
			for row in reader:
			    csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
			write_json(csv_rows, json_file, format)

#Convert csv data into json and write it
def write_json(data, json_file, format):
    print("Writing"+json_file)	
    with open(json_file, "w") as f:
        if format == "pretty":
            f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
        else:
            f.write(json.dumps(data))

if __name__ == "__main__":
   main()
