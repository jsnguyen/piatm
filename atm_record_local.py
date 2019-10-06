from time import sleep
import json
import urllib.request
import numpy as np
from sensors import get_all_sensor_data

period = 60 # seconds between measurements
output_filename = 'atm_data_local.dat'

print('Recording data locally...')

while True:
    data = get_all_sensor_data()
    time = data['time'] # unix time
    temp = np.mean(data['temp']) # fahrenheit
    humidity = data['humidity'] # percentage
    pressure = data['pressure'] # pascals

    with open(output_filename, 'a+') as f:
        f.write(str(time) +' '+ str(temp)+' '+ str(pressure)+' '+ str(humidity) + '\n')

    sleep(period)
