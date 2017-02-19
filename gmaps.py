import googlemaps
from datetime import datetime


# origin and dest should be in the format of a string with the lon and lat as 'lon,lat' 
# sydney town hall :
# '-33.8732,151.2061'

def requiredArg (origin,dest):
	gmaps = googlemaps.Client(key='AIzaSyCa0OIq7kHz5maDSHgvyZSosDg98Zc6kbI')	
	print googlemaps.convert.latlng(origin)
	file = open("./sample_json","w")
	file.write(str(gmaps.directions(origin,
								dest,
                               	mode="walking")))
	# print direction_result[0]

requiredArg ('-33.8732,151.2061' , '-33.0732,151.0061')
