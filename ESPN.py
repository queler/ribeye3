# # RBI Baseball 3 - ROM Modifier
# Joel Hill
# December 2013

"""
A test file to access the ESPN api

Limits:

3 calls per second
7,500 calls per day

The format of an API request is as follows:
http://api.espn.com/:version/:resource/:method?apikey=:yourkey
"""
import urllib.request
import urllib.parse
import json

application = "RBI Rom Modifier"
key = "nkyqeh6h837wpar74s5gt8e3"
secret = "SxA444SEcPAKz7BsznmneSCj"

url = "http://api.espn.com/v1/sports/baseball/mlb/teams"
full_url = url + "?apikey="+key
response = urllib.request.urlopen(full_url).read()
jsonResponse = json.loads(response.decode('utf-8'))
print(jsonResponse)

