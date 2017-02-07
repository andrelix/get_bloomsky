# NAME
# get_bloomsky.py - get data from BloomSky API for your API Key and save to file
#
# SYNOPSIS
# python get_bloomsky.py
#
# NOTE
# You will get errors if you don't change the value of api_key variable below to your API Key
# from http://dashboard.bloomsky.com/user/ Developer link
#
# FILES
# writes a pretty printed JSON file to the data_directory 'data' with the filename
# such as 1486445802_20170206-213642-PST.json
#
# CAVEATS
# This script is provided "as-is" with no warranty as to it's accuracy, suitability, or usefulness.
# Use at your own risk.
#
# REFERENCES
# BloomSky API Documentation v1.3
# http://weatherlution.com/.../BloomskyDeviceOwnerAPIDocume... 
#
import urllib2
import json
import time
import os

api_key = '...' # replace ... with API Key from http://dashboard.bloomsky.com/user/ Developer link
data_directory = 'data'

request = urllib2.Request('http://api.bloomsky.com/api/skydata/')
request.add_header('Authorization', api_key)

response = urllib2.urlopen(request)
content = response.read()

bs_data = json.loads(content)

timestamp = int(bs_data[0]['Data']['TS'])

ts = time.localtime(timestamp)

ts_text = str(timestamp) + '_' + time.strftime('%Y%m%d-%H%M%S-%Z',ts)

data_filename = data_directory + '/' + ts_text + '.json'

try:
os.mkdir('data')
except:
pass

with open(data_filename, 'w') as f:
f.write(json.dumps(bs_data, indent=4))
