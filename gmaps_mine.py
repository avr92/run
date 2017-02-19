import googlemaps
from datetime import datetime


# origin and dest should be in the format of a string with the lon and lat as 'lon,lat' 
# sydney town hall :
# '-33.8732,151.2061'

def isLat(g,i):
	return (g[i] == "'" and g[i+1] == "l" and g[i+2] == "a" and g[i+3] == "t" and g[i+4] == "'")

def isLon(g,i):
	return (g[i] == "'" and g[i+1] == "l" and g[i+2] == "n" and g[i+3] == "g" and g[i+4] == "'")

lat = []
lon = []

def find_all_lat_lon(data):
	for g in data.split(","):
		for i in range(0,len(g)-4):
			if isLat(g,i):
				new_lat = g[i+7:]
				lat.append(new_lat)
				break
			if isLon(g,i):
				new_lon = g[i+7:-1]
				lon.append(new_lon.strip('}'))
				break

def requiredArg (origin,dest):
	gmaps = googlemaps.Client(key='AIzaSyCa0OIq7kHz5maDSHgvyZSosDg98Zc6kbI')	
	print googlemaps.convert.latlng(origin)
	file = open("./sample_json","w")
	direction_result = gmaps.directions(origin,
								dest,
                               	mode="walking")
	g = str(direction_result[0]['legs'])
	find_all_lat_lon(g)

requiredArg ('-33.8732,151.2061' , '-33.0732,151.0061')
print len(lat)
print lat
print len(lon)
print lon