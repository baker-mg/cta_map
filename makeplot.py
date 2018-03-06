import math
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from xml.etree.ElementTree import parse
import time
from urllib.request import urlopen


my_map = Basemap(projection='merc', lat_0=41, lon_0=-87,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-88, llcrnrlat=41.6,
    urcrnrlon=-87.42, urcrnrlat=42.05)

my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color='coral')
my_map.drawmapboundary()


for i in range(120):
    u = urlopen("http://ctabustracker.com/bustime/map/getBusesForRouteAll.jsp")
    #data = u.read()
    doc = parse(u)

#doc = parse("data/allRoutes2018-03-06 18-41-08-722616.xml")

    for bus in doc.findall('bus'):
        lat = float(bus.findtext('lat'))
        lon = float(bus.findtext('lon'))
        x, y = my_map(lon, lat)
        my_map.plot(x, y, 'bo', markersize=1)

    print(i)
    time.sleep(30)
plt.show()

#https://imgur.com/a/70qzF