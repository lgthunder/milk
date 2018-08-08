# coding: utf-8
import urllib.request
import time
import sys
import re

token='0075000661cf21ad1340e49c4623eed6d405cbe1'

itemid=''

yidong='1'
liantong='2'
dianxin='3'
success_='success'
failure_='failure'

timeout_=60
step_=4
isShowApiLog=False

url='http://api.fxhyd.cn/UserInterface.aspx?'

login_='login&format=1'

account_info ='getaccountinfo&format=1'

getPhoneNumber_='getmobile'

getPhoneNumber_identifying='getsms'

release_phone='release'

add_ignore='addignore'

def setItemId(id):
	itemid=id
	pass

def getApi(action):
	return url+'action='+action+"&token="+token

def get(url):
	if isShowApiLog:
		print('request:'+ url)
	data = urllib.request.urlopen(url).read()
	str(data, encoding='utf-8')
	data=bytes.decode(data)
	if isShowApiLog:
		print('response:'+data)
	if success_ in data:
		return data
	else:
		return data

def login(name,pd):
	url=getApi(login_)
	url=url+'&username='+name+'&password='+pd
	get(url)


def getAccountInfo():
	url = getApi(account_info)
	get(url)


def getPhoneNumber(itemid,isp,province,city,mobile,excludeno):
	url=getApi(getPhoneNumber_)+'&itemid='+itemid+'&excludeno='+excludeno+'$isp='+isp+'&province='+province+'&city='+city+'&mobile='+mobile
	data= get(url)
	return decodePhoneNumber(data)

def getProvince():
	pass

def decodeResponse(response):
	data=response.split('|',1)
	if len(data)>1:
		return data[1]
	else:
		return data	

def decodePhoneNumber(response):
	data=response.split('|',len(response))
	if len(data)>1:
		return data[1]
	else:
		return data

def releaseNumber(itemid,num):
	url=getApi(release_phone)+'&itemid='+itemid+'&mobile='+num
	get(url)

def getIdentifyingCode(itemid,mobile,release):
	url=getApi(getPhoneNumber_identifying)+'&itemid='+itemid+'&mobile='+mobile+'&release='+release
	return get(url)

def addIgnore(itemid,mobile):
	url=getApi(add_ignore)+'&itemid='+itemid+'&mobile='+mobile
	pass

def waitIdentifyingCode(itemid,mobile,release):
	count=0;
	while count<timeout_:
		result=getIdentifyingCode(itemid,mobile,release)
		if result == '3001'or result=='3002'or result=='3003'or result=='3004': #尚未收到短信
			count=count+step_
			time.sleep(step_)
		elif result.split('|')[0] == "success":
			decodeIdentifyCode(result.split('|')[1])
			break	
		else: #号码已被释放
			break
		pass
	pass

def decodeIdentifyCode(text):
	pat = "[0-9]+"
	IC = 0
	IC = re.search(pat, text)
	if IC:
    	 return IC.group()
	else:
    	 print("表达式错误")
	pass	

# setItemId('21584')
# itemid='21584'
# print(sys.argv[1])
# getPhoneNumber(itemid,yidong,'220000','','','171')
# getAccountInfo()
# decodePhoneNumber('success|15948092148|2121|3123123')
# releaseNumber(itemid,'17014323161')
# waitIdentifyingCode(itemid,'18444079497','1')
# decodeIdentifyCode('【火牛】验证码938944，请在5分钟内使用，请确保是本人操作且为本人手机')
