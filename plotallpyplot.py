import matplotlib.pyplot as plt
import numpy as np
from xml.etree.ElementTree import parse
import os
# most buses on at once = 1374

count = 1

for file in os.listdir(os.getcwd()+'/data'):
    allatt = []
    doc = parse("data/{}".format(file))
    for bus in doc.findall('bus'):
        lat = float(bus.findtext('lat'))
        lon = float(bus.findtext('lon'))
        allatt.append([lon, lat])
    npallatt = np.asarray(allatt)
    fig = plt.figure(frameon=False)
    fig.set_size_inches(20,20)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()

    hb = ax.hexbin(npallatt[:,0], npallatt[:,1], gridsize=500, bins='log', cmap='inferno', extent=(-87.5, -87.9, 41.6, 42.1))
    fig.add_axes(ax)
    ax.axis('equal')
    plt.axis('off')
    plt.savefig("hm{}.png".format(count), transparent = True, bbox_inches='tight', pad_inches=0.0)
    plt.close()
    count += 1