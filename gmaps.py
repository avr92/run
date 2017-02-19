import googlemaps
from datetime import datetime
import polyline

# origin and dest should be in the format of a string with the lon and lat as 'lon,lat' 
# sydney town hall :
# '-33.8732,151.2061'

def requiredArg (origin,dest):
	gmaps = googlemaps.Client(key='AIzaSyCa0OIq7kHz5maDSHgvyZSosDg98Zc6kbI')	
	print googlemaps.convert.latlng(origin)
	# file = open("./sample_json","w")
	# file.write(str())
	direction_result = gmaps.directions(origin,
								dest,
                               	mode="walking")
	print len(direction_result[0])
	print direction_result[0]
	print len(direction_result[0]["legs"][0])
	print len(direction_result[0]["legs"][0]["steps"])
	ct = 0
	for j in range(len(direction_result[0]["legs"])):
		for i in range(len(direction_result[0]["legs"][0]["steps"])):
			ct += 1
			print polyline.decode(direction_result[0]["legs"][j]["steps"][i]["polyline"]["points"])
			print direction_result[0]["legs"][j]["steps"][i]["start_location"] , direction_result[0]["legs"][j]["steps"][i]["duration"] , direction_result[0]["legs"][j]["steps"][i]["end_location"]
	print ct
	# print direction_result[0]["legs"][0]["start_location"] , direction_result[0]["legs"][0]["duration"] , direction_result[0]["legs"][0]["duration"]

requiredArg ('-33.8732,151.2061' , '-33.0732,151.0061')
