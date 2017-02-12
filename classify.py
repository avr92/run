from geopy.distance import vincenty
import statsmodels.formula.api as sm
import datetime
import pandas as pd
import random 
from sklearn.linear_model import LinearRegression

def f(user_tracks):
	length = []
	user = []
	disruptions = []
	labels = ['Length', 'User', 'Disruption']

	for track in user_tracks:
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

	for i in range(0,len(y)):
		if y_pred > 0.4:
	
	# df = pd.DataFrame.from_records(datas,columns=labels)
	# print df

	# res = sm.ols(formula="y~length+user+disruptions",data=df).fit()

	# print res.summary()
