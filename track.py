# coding: utf-8

def getTrack(distance):
	distance+=30 #先滑过一点，最后再反着滑动回来
	v=0
	t=0.2
	forward_tracks=[]

	current=0
	mid=distance*3/5
	while current < distance:
	    if current < mid:
	        a=1800
	    else:
	        a=-2600

	    s=v*t+0.5*a*(t**2)
	    v=v+a*t
	    current+=s
	    forward_tracks.append(round(s))

	#反着滑动到准确位置
	back_tracks=[-5,-10,-15,-5] #总共等于-20

	return {'forward_tracks':forward_tracks,'back_tracks':back_tracks}
	pass

# print(getTrack(720))