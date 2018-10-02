# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:23:36 2018

@author: HIMANSHU
"""
import cv2

def main():
    imgpath="C:\\Users\\HIMANSHU\\Desktop\\OpenCV_Dataset\\standard_test_images\\cameraman.tif"
    img=cv2.imread(imgpath)
    outpath="C:\\Users\\HIMANSHU\\Desktop\\OpenCV_Dataset\\hc.jpg"
    cv2.namedWindow('Cameraman', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Camraman', img)
    cv2.imwrite(outpath, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows('Cameraman')
    
    
if __name__=="__main__":
    main()
