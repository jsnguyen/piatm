from time import sleep
import json
import urllib.request
import numpy as np

filename='data.dat'
counter=0
length = 4*60*60
temp=[]
while True:
    data = json.loads(urllib.request.urlopen("http://10.0.0.111:8000/data/").read())
    time = data['time']
    temp = np.mean(data['temp'])
    humidity = data['humidity']
    pressure = data['pressure']

    with open(filename, 'a') as f:
        f.write(str(time) +' '+ str(temp)+' '+ str(pressure)+' '+ str(humidity) + '\n')

    if counter > length:
        break

    if counter%5 == 0:
        print(counter,'of',length)

    counter+=1
    sleep(1)
