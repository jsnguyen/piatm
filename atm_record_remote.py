from time import sleep
import json
import urllib.request
import numpy as np

server_ip = 'http://10.0.0.66:8000/'
period = 60 # seconds between measurements
output_filename = 'atm_data_remote.dat'

print('Recording data from server...')

while True:
    data = json.loads(urllib.request.urlopen(server_ip).read())
    time = data['time'] # unix time
    temp = np.mean(data['temp']) # fahrenheit
    humidity = data['humidity'] # percentage
    pressure = data['pressure'] # pascals

    with open(output_filename, 'a+') as f:
        f.write(str(time) +' '+ str(temp)+' '+ str(pressure)+' '+ str(humidity) + '\n')

    sleep(period)
