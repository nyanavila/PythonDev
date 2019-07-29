#!/bin/bash/python3.6

import json
import urllib.request

pb = urllib.request.urlopen('https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD')
pb_body = pb.read()

#f = open("rows.json", "r")

y = json.loads(pb_body.decode("utf-8"))

#in_json = json.load(y)
#print(json.dumps(y))
#print(y["data"][0][9]+ " :  " + y["data"][0][8] + " : " + y["data"][0][10])

for x in y["data"]:
  print(x[9])
