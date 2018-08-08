import cv2 as cv
import numpy as np
import imutils
import math
isDebug=False
 
def edge(img):
    #高斯模糊,降低噪声
    blurred = cv.GaussianBlur(img,(3,3),0)
    #灰度图像
    gray=cv.cvtColor(blurred,cv.COLOR_RGB2GRAY)
    #图像梯度
    xgrad=cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygrad=cv.Sobel(gray,cv.CV_16SC1,0,1)
    #计算边缘
    #50和150参数必须符合1：3或者1：2
    edge_output=cv.Canny(xgrad,ygrad,50,100)
    #图一
    # cv.imshow("edge",edge_output)
    return edge_output
    # dst=cv.bitwise_and(img,img,mask=edge_output)
    #图二（彩色）
    # cv.imshow('cedge',dst)

def getShadowPos(path,min,max,tolerance):

    src=cv.imread(path)
    #图三（原图）
    # cv.imshow('def',src)
    thresh=edge(src)
    image =thresh
    # find contours in the thresholded image
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL,
        cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    print(len(cnts))
    # loop over the contours
   
    shapeList=[]
    for c in cnts:
        # compute the center of the contour
        M = cv.moments(c)
        if M["m00"]==0:
            continue
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
 
        # draw the contour and center of the shape on the image

    
        #－－－－－－＃
        # 用绿色(0, 255, 0)来画出最小的矩形框架  
        x, y, w, h = cv.boundingRect(c)  
        if w<min or h <min :
            continue
        elif w>max or h>max:
            continue
        shapeList.append([x,y,w,h])    
        # if len(keyList) ==0:
        #     keyList.append(y)
        #     targetMap[str(y)]=[[x,y,w,h]]
        # else:
        #     flag =False
        #     for yy in keyList:
        #         if abs(yy-y)<tolerance:
        #             targetMap[str(yy)].append([x,y,w,h])
        #             flag=True
        #             break
                    
        #     if not flag:
        #         keyList.append(y)
        #         targetMap[str(y)]=[[x,y,w,h]] 
           
        if isDebug:	
            # print(y)      
            # print(w)
            # print(h)
            cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)  
  
            # 用红色表示有旋转角度的矩形框架  
            rect = cv.minAreaRect(c)  
            box = cv.boxPoints(rect)  
            box = np.int0(box)  
            cv.drawContours(image, [box], 0, (0, 0, 255), 2)  

            cv.drawContours(image, [c], -1, (0, 255, 0), 2)
            cv.circle(image, (cX, cY), 7, (255, 255, 255), -1)
            cv.putText(image, "center", (cX - 20, cY - 20),
                cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
 
            # show the image
            cv.imshow("Image", image)
            cv.waitKey(0)

    # for key in keyList:
    #     print('key length '+str(len(targetMap[str(key)])))
    #     if len(targetMap[str(key)])<2:
    #         continue
    #     result=compareWH(targetMap[str(key)])
    #     if result>0:
    #         return result
    #     else:
    #         return -1;    

    return findSimilarShape(shapeList,tolerance)
     
def findSimilarShape(shapeList,tolerance):
    targetMap ,keyList=sorft(shapeList,1,tolerance)
    # for c in shapeList:
    #     x,y,w,h=c
    #     if len(keyList) ==0:
    #         keyList.append(y)
    #         targetMap[str(y)]=[[x,y,w,h]]
    #     else:
    #         flag =False
    #         for yy in keyList:
    #             if abs(yy-y)<tolerance:
    #                 targetMap[str(yy)].append([x,y,w,h])
    #                 flag=True
    #                 break
                
    #         if not flag:
    #             keyList.append(y)
    #             targetMap[str(y)]=[[x,y,w,h]] 

    for key in keyList:
        if len(targetMap[str(key)])<2:
            continue
        wlist=filter(targetMap[str(key)],2,tolerance)
        if wlist:
            hlist=filter(wlist,3,tolerance)
            if hlist:
                result=compareWH(hlist)        
                if result>0:
                    return result
                else:
                    return -1
    return -1

def filter(shapeList,index,tolerance):
    targetMap ,keyList=sorft(shapeList,index,tolerance)
    for key in keyList:
        if len(targetMap[str(key)])<2:
            continue
        else:
            return targetMap[str(key)]

def sorft(shapeList,index,tolerance):
    targetMap ={}
    keyList=[]
    for c in shapeList:
        key=c[index]
        if len(keyList) ==0:
            keyList.append(key)
            targetMap[str(key)]=[c]
        else:
            flag =False
            for yy in keyList:
                if abs(yy-key)<tolerance:
                    targetMap[str(yy)].append(c)
                    flag=True
                    break
                
            if not flag:
                keyList.append(key)
                targetMap[str(key)]=[c]
    return targetMap,keyList

def compareWH(result):
    if len(result)==2:
        print(result[0])
        print(result[1])
        return abs(result[0][0]-result[1][0])
    # for index in result:
        # print(index)

