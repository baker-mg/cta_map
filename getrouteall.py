from urllib.request import urlopen
from datetime import datetime
import time

for i in range(180):
    u = urlopen("http://ctabustracker.com/bustime/map/getBusesForRouteAll.jsp")
    data = u.read()
    with open("data/allRoutes{}.xml".format(str(datetime.now()).replace(":", "-").replace(".", "-")), 'wb') as file:
        file.write(data)
    u.close()
    time.sleep(60)
