# format .json file into .txt

import json
import sys
import os

writeIGfile = open("instagram.txt","w")
writeTWTfile = open("twitter.txt","w")
writeYTfile = open("youtube.txt","w")
writeFBfile = open("facebook.txt","w")

path_to_json = "raw_json/"
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

for file_name in json_files:
     with open(path_to_json + file_name) as json_file:
        data = json.load(json_file)

        if ("instagram" in file_name):
            writeIGfile.write(json.dumps(data))
            writeIGfile.write("\n")
        elif ("twitter" in file_name):
            writeTWTfile.write(json.dumps(data))
            writeTWTfile.write("\n")
        elif ("youtube" in file_name):
            writeYTfile.write(json.dumps(data))
            writeYTfile.write("\n")
        elif ("facebook" in file_name):
            writeFBfile.write(json.dumps(data))
            writeFBfile.write("\n")

writeFBfile.close()
writeYTfile.close()
writeTWTfile.close()
writeIGfile.close()