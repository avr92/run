import gpxpy
import gpxpy.gpx
from geopy.distance import vincenty
import random
import math
import time
import datetime
import thread
from classify import f

tracks = []
user_tracks = []

class GPX_Object:
	"""A simple example class"""
	miles = 0
	user = 0
	gpx = None
	pace = 0
	gps_start = 0
	gps_end = 0
	def __init__(self,node=None,m=None,p=None):
		self.gpx = node
		self.miles = m
		self.pace = p
		#self.gps_start, self.gps_end = ret_start_stop(self)
		print 'Hello World'

	def display_track(self):
		for track in self.gpx.tracks: 
			print track
			for segment in track.segments: 
				print segment
				for point in segment.points: 
					pass
					#print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

	def ret_start_stop(self):
		i = 0
		for track in self.gpx.tracks: 
			for segment in track.segments: 
				x = len(segment.points)
				for point in segment.points: 
					if i == 0:
						self.gps_start = (point.latitude, point.longitude)
					if i == x-1:
						self.gps_end = (point.latitude, point.longitude)
					i += 1


	def display_waypoint(self):
		for waypoint in self.gpx.waypoints:
			print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude) 

	def display_routes(self):
		for route in self.gpx.routes:
			print 'Route:' 
			for point in route: 
				print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)

range = 2
user_location = (42.364506,-71.038887)

def find_tracks(location):
	print "Started executing find_tracks"
	for track_user in tracks:
		flag = 0
		for track in track_user.gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					start = (point.latitude, point.longitude)
					if vincenty(location, start).miles < range:
						flag = 1
						break
		if flag == 1:
			user_tracks.append(track_user)


def generate_tracks():
	for i in xrange(0,1000):
		f = random.randint(0,2)
		if f == 1:
			flag = 1
		else:
			flag = 0
		g, m = generate_track(flag)
		track = GPX_Object(g,m)
		u = random.randint(1,5)
		if u != 4:
			track.user = u
		else:
			track.user = 1
		tracks.append(track)


def generate_track(flag):
	TOTAL_RUNNERS = 100;

	b_lon = -71.035887
	b_lat = 42.367506

	gpx = gpxpy.gpx.GPX()
	gpx_track = gpxpy.gpx.GPXTrack()
	gpx_segment = gpxpy.gpx.GPXTrackSegment()
	mult = 0.01
	rand_lon = random.randint(-20,20)*mult
	rand_lat = random.randint(-20,20)*mult
	j=0;
	curr_time = datetime.datetime.utcnow()
	total_segs = random.randint(50,100)
	for i in xrange(0,total_segs):
		run_by =  random.uniform(0.0003, 0.0005);
		g = datetime.timedelta(0,1)
		if flag == 1:
			r = random.randint(1,8)
			if i >= total_segs/2 and r == 4:
				g = datetime.timedelta(0,random.randint(50,100))
		curr_time = curr_time + g
		gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(b_lat+rand_lat+j, b_lon+rand_lon+j, elevation=1.1, time=curr_time))
		#THE code snipet for time
		j=j+run_by;

	gpx_track.segments.append(gpx_segment)
	gpx.tracks.append(gpx_track)
	start = (b_lat+rand_lat, b_lon+rand_lon)
	end = (b_lat+rand_lat+j, b_lon+rand_lon+j)
	print(vincenty(start, end).miles)
	return gpx, vincenty(start, end).miles


generate_tracks()
find_tracks(user_location)
print len(user_tracks)
f(user_tracks)
#find_tracks(0)

#print vincenty((42.4015264233,-71.035887),(42.4018264233,-71.035287))



'''

gpx_file1 = open('./NewData.gpx')
gpx_file = open('/Users/arima/Documents/PDP/run/anthony_activities/20150904-005109-Run.gpx', 'r') 




gpx = gpxpy.parse(gpx_file) 
# a = GPX_Object(gpx)
# a.display_track()



#print isinstance(gpx, )

print type(gpx)

for track in gpx.tracks: 
	for segment in track.segments: 
		for point in segment.points: 
			print 'Point at ({0},{1}) -> {2} @ {3}'.format(point.latitude, point.longitude, point.elevation,point.time) 

for waypoint in gpx.waypoints: 
	print 'waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude) 

for route in gpx.routes: 
	print 'Route:' 
	for point in route: 
		print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation) 


print 'GPX:', gpx.to_xml()

print type(gpx.to_xml())

#st = open('./NewData.gpx','w')
#st.write(gpx.to_xml())
'''

