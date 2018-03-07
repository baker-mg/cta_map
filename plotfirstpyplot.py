import matplotlib.pyplot as plt
import numpy as np
from xml.etree.ElementTree import parse
import os
# most buses on at once = 1374
allatt = []
#for file in os.listdir(os.getcwd()+'/data'):
file = "allRoutes2018-03-06 22-27-06-194613.xml"
doc = parse("data/{}".format(file))
np.empty([1374, 2])
for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    lon = float(bus.findtext('lon'))
    allatt.append([lon, lat])
npallatt = np.asarray(allatt)
print(npallatt)
fig1, ax1 = plt.subplots(figsize = (16, 8))
ax1.scatter(npallatt[:,0], npallatt[:,1], alpha=0.05)
ax1.axis([-87.3, -87.9, 41.5, 42.1])
plt.gca().invert_xaxis()
ax1.autoscale(enable=True, axis='both')
plt.show()



