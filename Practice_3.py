# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 21:50:44 2018

@author: HIMANSHU
"""
import cv2
import numpy as np

windowName='Drawing'
img=np.zeros((512,512,3), np.uint8)
cv2.namedWindow(windowName)
drawing =False

def main():
    while(True):
        cv2.imshow(windowName,img)
        if cv2.waitKey(20)==27:
            break
    cv2.destroyAllWindows()


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)

cv2.setMouseCallback(windowName,draw_circle)

if __name__=="__main__":
    main()