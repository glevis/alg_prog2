import math

def haversine(lat1, long1, lat2, long2):
	
	radiusOfEarthInMiles = 3958.8
	
	lat1Radians = math.radians(float(lat1))
	long1Radians = math.radians(float(long1))
	lat2Radians = math.radians(float(lat2))
	long2Radians = math.radians(float(long2))
	
	a = pow(math.sin((lat2Radians-lat1Radians)/2), 2) + math.cos(lat1Radians)*math.cos(lat2Radians)*pow(math.sin((long2Radians-long1Radians)/2), 2)
	c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
	
	return radiusOfEarthInMiles*c
