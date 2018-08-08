# coding: utf-8
import handle
from phone_frame import Frame
import yima_api
import time
from PIL import Image
import os
import canny
import track
huoniu_code='1634011'
hab_code='MJQ9X3'
huoniu_item_id='21219'
file_dir='./temp/'

class huoniu(Frame):
	def getPhonePos(self):
		return [700,646]

	def getSendIndentifyPos(self):
		return [1200,860]

	def getIndentifyInputPos(self):
		return [720,833]

	def getLoginPos(self):
		return [720,1320]

	def getClearPhonePos(self):
		return [1270,640]

	def getInviteInputPos(self):
		return [300,1050]

	def getIdentifyPic(self,name):
		return handle.getScreenShort(name)

	def getIdentifyPicAra(self):
		return [250,940,1200,1470]
		pass

def click(pos):
	handle.tap(pos[0],pos[1])
	pass

def input(text):
	handle.text(text)
	pass


def swapIndentify(mobile):
	distance =-1
	while distance<0:
		distance =decodeIndentifyPic(mobile)
		if distance<0:
			handle.tap(1043,1660)
			time.sleep(3)
	print(distance)
	stepList=track.getTrack(distance)
	pos=[422,1555]
	# for step in stepList['forward_tracks']:
	# 	print(step)
	# 	print(pos)
	# 	pos=swapBy(pos,step)
	# 	pass
	# pos=swapBy(pos,distance+30)
	# swapBy(pos,-30)
	pass


def decodeIndentifyPic(mobile):
	temp =file_dir+'%s.png'%str(mobile)
	h.getIdentifyPic(mobile)
	img = Image.open(temp) 
	region = img.crop(h.getIdentifyPicAra())
	path =file_dir+"crop_{}.png".format(mobile)
	region.save(path)
	os.remove(temp)
	distance = canny.getShadowPos(path,100,150,5)
	return distance

def swapBy(pos,step):
	nexPos=[pos[0]+step,pos[1]]
	handle.swipe(pos,nexPos)
	return nexPos

def testIndentifyPic(path):
	distance =getShadowPos('crop_2312312312.png',120,150,5)
	print(distance)

# handle.open('com.waqu.android.firebull/.ui.LoginActivity')
# click(clear_phone_text)
# click(phone_text)
# input('312312312')
# click(lucky_text)
# input(lucky_code)

h= huoniu()
mobile='2312312312'
# click(h.getClearPhonePos())
# click(h.getPhonePos())
# print('获取手机号')
# mobile=yima_api.getPhoneNumber(huoniu_item_id,yima_api.yidong,'220000','','','171')
# print('输入手机号'+mobile)
# input(mobile)
# print('输入邀请码'+huoniu_code)
# click(h.getInviteInputPos())
# input(huoniu_code)
# print('获取验证码')
# click(h.getSendIndentifyPos())
# print('释放手机号'+mobile)
# yima_api.releaseNumber(huoniu_item_id,mobile)
# time.sleep(4)
swapIndentify(mobile)






