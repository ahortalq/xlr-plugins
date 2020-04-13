import urllib2
import urllib
import json

url = valueProvider.dockerhubServer.url
auth = urllib.urlencode({'username': valueProvider.dockerhubServer.username, 'password': valueProvider.dockerhubServer.password})
request = urllib2.Request(url + "/v2/users/login", auth)
response = urllib2.urlopen(request)
data = json.load(response)
request = urllib2.Request(url + "/v2/repositories/" + valueProvider.dockerhubServer.username + "/?page_size=100")
request.add_header("Authorization", "JWT %s" % data['token'])
response = urllib2.urlopen(request)
data = json.load(response)
result = []
for i in data['results']:
    result = result + [i['name']]
