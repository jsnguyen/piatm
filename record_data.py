from time import sleep
import json
import urllib.request
import numpy as np

counter=0
f_counter=0
length = 24*60*60
datastr=[]
while True:
    data = json.loads(urllib.request.urlopen("http://10.0.0.111:8000/data/").read())
    time = data['time']
    temp = np.mean(data['temp'])
    humidity = data['humidity']
    pressure = data['pressure']

    line = str(time) +' '+ str(temp)+' '+ str(pressure)+' '+ str(humidity) + '\n'
    datastr.append(line)

    if len(datastr) == 10:
        with open('data_'+str(f_counter)+'.dat', 'w') as f:
            for el in datastr:
                f.write(el)
            datastr=[]
            f_counter+=1

    if counter%5 == 0:
        print(counter,'of',length)

    counter+=1
    sleep(1)
