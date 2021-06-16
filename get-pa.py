#!env python3
#
# get the json from purpleair, averaging the two AQI elements
#

import requests
URL = "http://purpleair-d32a/json"

try:
    r = requests.get(url=URL)
except:
    print("ERROR - cannot get url:" , URL)

data = r.json()

aqi_a = data['pm2.5_aqi']
aqi_b = data['pm2.5_aqi_b']

color_a = data['p25aqic']
color_b = data['p25aqic_b']

try:
    aqi_ave = int( (aqi_a + aqi_b)/2 )
    print(aqi_a,aqi_b,aqi_ave)
    print(color_a,color_b)
except:
    print("ERROR - one sensor not returning ann int")
    print(aqi_a,aqi_b)

