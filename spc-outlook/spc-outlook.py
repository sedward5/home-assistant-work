import json
from shapely.geometry import shape, Point
import requests
location = Point(-83, 42) # add your lon lat here
for day in range(1, 4):
    print('Day '+str(day)+' outlook:')
    url = 'https://www.spc.noaa.gov/products/outlook/day' + str(day) + 'otlk_cat.lyr.geojson'
    result = False
    resp = requests.get(url=url)
    data = resp.json()
    #print(data)
    for feature in data['features']:
        polygon = shape(feature['geometry'])
        #print(feature)
        if polygon.contains(location):
            print('Day ' + str(day) + ' Categorical Risk: ', feature['properties']['LABEL2'])
            result = True
    if result and day < 3:
        torn_url = 'https://www.spc.noaa.gov/products/outlook/day' + str(day) + 'otlk_torn.lyr.geojson'
        resp = requests.get(url=torn_url)
        data = resp.json()
        for feature in data['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(location):
                print('Tornado risk: ', feature['properties']['LABEL2'])
        hail_url = 'https://www.spc.noaa.gov/products/outlook/day'+str(day)+'otlk_hail.lyr.geojson'
        resp = requests.get(url=hail_url)
        data = resp.json()
        for feature in data['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(location):
                print('Hail risk: ', feature['properties']['LABEL2'])
        wind_url = 'https://www.spc.noaa.gov/products/outlook/day'+str(day)+'otlk_wind.lyr.geojson'
        resp = requests.get(url=wind_url)
        data = resp.json()
        for feature in data['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(location):
                print('Wind risk: ', feature['properties']['LABEL2'])