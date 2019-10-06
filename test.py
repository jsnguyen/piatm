import urllib.request,json

url="http://10.0.0.66:8000/"

with urllib.request.urlopen(url) as u:
	data = json.loads(u.read().decode())
	print (data['temp'])
