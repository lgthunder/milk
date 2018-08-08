# coding: utf-8
import os
import shutil

work_path = os.getcwd()
order_start = work_path + '/file/adb.exe '


def open(luanch):
	system_cmd('shell su am start -n '+luanch)
	pass

def tap(x,y):
	system_cmd('shell input tap %d %d' % (x,y))
	pass

def swipe(start_x,start_y,end_x,end_y):
	system_cmd('shell input swipe %d %d %d %d' % (start_x,start_y,end_x,end_y))
	pass

def swipe(current_pos,next_pos):
	system_cmd('shell input swipe %d %d %d %d' % (current_pos[0],current_pos[1],next_pos[0],next_pos[1]))
	pass

def text(text):
	system_cmd('shell input text '+text)
	pass	

def getScreenShort(name):
    path = './temp/%s.png'%name
    print('start delete cache')
    if os.path.exists(path):
        shutil.copy(path,'temp/last_%s.png'%name)
        os.remove(path)
    print('start screen short')
    while True:
        print("开始截屏...", end="")
        system_cmd('shell screencap -p /sdcard/%s.png' % str(name))
        system_cmd('pull /sdcard/%s.png ./temp' % str(name))
        if os.path.exists(path):
            print("完成!")
            return True
        else:
            input("获取截图失败，请检查手机是否连接到电脑，并是否开启开发者模式,回车继续")



def system_cmd(cmd):
    mac_os(cmd)

def mac_os(cmd):
    os.system('adb '+cmd)

def win_os(cmd):
     _cmd(order_start+cmd)

