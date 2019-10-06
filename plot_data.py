import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

filename = 'data.dat'

time=[]
temp=[]
pressure=[]
humidity=[]
with open(filename) as f:
    for line in f:
        l = line.split()
        time.append(datetime.fromtimestamp(float(l[0])))
        temp.append(float(l[1]))
        pressure.append(float(l[2]))
        humidity.append(float(l[3]))

plt.plot(time,temp)
plt.show()
