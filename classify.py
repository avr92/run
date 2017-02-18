from geopy.distance import vincenty
import statsmodels.formula.api as sm
import datetime
import pandas as pd
import random 
from sklearn.linear_model import LinearRegression
import webbrowser

def change(gps):
	return "{0},{1}".format(gps[0],gps[1])

def f(user_tracks):
	length = []
	user = []
	disruptions = []
	labels = ['Length', 'User', 'Disruption']

	for j in xrange(0,len(user_tracks)):
		track = user_tracks[j]
		track.ret_start_stop()
		length.append(vincenty(track.gps_start, track.gps_end).miles)
		user.append(track.user)
		i = 0
		flag = 1
		disp = 0
		for track in track.gpx.tracks:
			for segment in track.segments:
				for point in segment.points:
					end = point.time
					if i != 0:
						if (end-start)<=datetime.timedelta(0, 1):   
							flag = 1
						else:
							disp += 1
					start = point.time
					if flag == 0:
						break
					i += 1
		disruptions.append(disp) 

	print length
	print disruptions
	print user

	datas = []
	y = []
	for i in range(0,len(length)):
		s = []
		s.append(length[i])
		s.append(user[i])
		s.append(disruptions[i])
		#s.append(random.randint(0,1))
		datas.append(s)
		y.append(random.randint(0,1))

	lm = LinearRegression()
	lm.fit(datas,y)
	y_pred = lm.predict(datas)
	print y
	print lm.score(datas,y)
	count = 0
	for i in range(0,len(y)):
		if y_pred[i] > 0.4:
			count += 1
	print "The number of tracks:{0}".format(count)
	for i in range(0,len(y)):
		if y_pred[i] > 0.4:

			gps_start = change(user_tracks[i].gps_start)
			gps_end = change(user_tracks[i].gps_end)
			webbrowser.open('http://demo-abhayk.rhcloud.com/?origin={0}&dest={1}'.format(gps_start,gps_end))
			g = raw_input("Press e to Exit...")
			if g == 'e' or g == 'E':
				break
