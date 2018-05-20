#coding:utf-8
import os
import cv2
from PIL import Image
import numpy as np


def getName(num):
    strTmp = []
    strRes = ''

    while(int(num / 10)): # 强制转换为int
        strTmp.append(num % 10)
        num = int(num / 10) # 强制转换为int
    strTmp.append(num)
    n = len(strTmp)
    for i in range(0,5-n):
        strRes = strRes + '0'
    for i in range(n-1,-1,-1):
        strRes = strRes + str(strTmp[i])
    return strRes

videoCapture = cv2.VideoCapture('VID_20180504_171047.mp4')
#获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)

print('码率为', fps)

size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

#读帧
if not os.path.exists('rgb/'):
    os.makedirs('rgb')
success, frame = videoCapture.read()
idx = 1
while success:
    # cv2.imshow("显示", frame) #显示
    cv2.waitKey(int(1000/int(fps))) #延迟
    print(cv2.imwrite('rgb/'+ getName(idx) +'.png',frame))
    success, frame = videoCapture.read() #获取下一帧
    idx = idx + 1