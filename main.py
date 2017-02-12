import gpxpy
import gpxpy.gpx
from geopy.distance import vincenty
import random
import math

tracks = []


class GPX_Object:
	"""A simple example class"""
	miles = 0
	gpx = None
	pace = 0
	gps_start = 0
	gps_end = 0
	def __init__(self,node=None,m=None,p=None):
		self.gpx = node
		self.miles = m
		self.pace = p
		self.gps_start, self.gps_end = ret_start_stop(self)
		print 'Hello World'

	def display_track(self):
		for track in gpx.tracks: 
			print track
			for segment in track.segments: 
				print segment
				for point in segment.points: 
					pass
					#print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

	def ret_start_stop(self):
		i = 0
		for track in gpx.tracks: 
			print track
			for segment in track.segments: 
				print segment
				x = len(segment.points)
				for point in segment.points: 
					if i == 0:
						start = (point.latitude, point.longitude)
					
					if i == x-1:
						end = (point.latitude, point.longitude)
		return start, end


	def display_waypoint(self):
		for waypoint in gpx.waypoints: 
			print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude) 

	def display_routes(self):
		for route in gpx.routes: 
			print 'Route:' 
			for point in route: 
				print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

range = 2


def find_tracks(location):
	for track in tracks:
		

def generate_tracks():
	for i in xrange(0,30):
		g, m = generate_track()
		track = GPX_Object(g,m)
		tracks.append(track)


def generate_track():
	TOTAL_RUNNERS = 100;

	b_lon = -71.038887
	b_lat = 42.364506

	gpx = gpxpy.gpx.GPX()
	gpx_track = gpxpy.gpx.GPXTrack()
	gpx_segment = gpxpy.gpx.GPXTrackSegment()

	rand_lon = random.randint(-20,20)
	rand_lat = random.randint(-20,20)
	j=0;
	total_segs = random.randint(50,200)
	for i in xrange(0,total_segs):
		run_by =  random.uniform(0.0001, 0.0003);
		gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(b_lat+rand_lat+j, b_lon+rand_lon+j, elevation=1.1))
		j=j+run_by;

	gpx_track.segments.append(gpx_segment)
	gpx.tracks.append(gpx_track)

	start = (b_lat+rand_lat, b_lon+rand_lon)
	end = (b_lat+rand_lat+j, b_lon+rand_lon+j)
	print(vincenty(start, end).miles)
	return gpx, vincenty(start, end).miles



gpx_file1 = open('./NewData.gpx')
gpx_file = open('/Users/arima/Documents/PDP/run/anthony_activities/20150904-005109-Run.gpx', 'r') 

generate_tracks()
find_tracks(0)


gpx = gpxpy.parse(gpx_file) 
a = GPX_Object(gpx)
a.display_track()




#print isinstance(gpx, )
'''
print type(gpx)

for track in gpx.tracks: 
	for segment in track.segments: 
		for point in segment.points: 
			print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation) 

for waypoint in gpx.waypoints: 
	print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude) 

for route in gpx.routes: 
	print 'Route:' 
	for point in route: 
		print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation) 


print 'GPX:', gpx.to_xml()

print type(gpx.to_xml())

st = open('./NewData.gpx','w')
st.write(gpx.to_xml())
'''

