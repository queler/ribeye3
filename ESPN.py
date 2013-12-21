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
version = "v1"


def request(ver, resource, method, k, values=()):
    if len(values) == 0:
        url = "http://api.espn.com/"+ver+"/"+resource+"/"+method+"?apikey="+k
    else:
        url_values = urllib.parse.urlencode(values)
        url = "http://api.espn.com/"+ver+"/"+resource+"/"+method+"?"+url_values+"&apikey="+k
    return urllib.request.urlopen(url).read()


def test_request():
    val = {}
    val['groups'] = '1'
    val['lang'] = 'es'
    #test with optional values
    print(request(version, "sports", "baseball/mlb/teams", key, val))
    #test without values added to request
    print(request(version, "sports", "baseball/mlb/teams", key))


test_request()