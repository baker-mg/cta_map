from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from xml.etree.ElementTree import parse
import os


count = 1

def makemap(file):
    my_map = Basemap(projection='merc', lat_0=41, lon_0=-87,
    resolution = 'h', area_thresh = 0.1,
    llcrnrlon=-88, llcrnrlat=41.6,
    urcrnrlon=-87.42, urcrnrlat=42.05)

    my_map.drawcoastlines()
    my_map.drawcountries()
    my_map.fillcontinents(color='coral')
    my_map.drawmapboundary()
    doc = parse("data/{}".format(file))
    for bus in doc.findall('bus'):
        lat = float(bus.findtext('lat'))
        lon = float(bus.findtext('lon'))
        x, y = my_map(lon, lat)
        my_map.plot(x, y, 'bo', markersize=1)
    plt.savefig("fig{}".format(count))
    plt.clf

for file in os.listdir(os.getcwd()+'/data'):
    makemap(file)
    count += 1