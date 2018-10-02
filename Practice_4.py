# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:11:57 2018

@author: HIMANSHU
"""
import cv2
import matplotlib.pyplot as plt

def main():
    imgpath="C:\\Users\\HIMANSHU\\Desktop\\OpenCV_Dataset\\standard_test_images\\lena_color_512.tif"
    img=cv2.imread(imgpath,0)
    
    plt.imshow(img, cmap='Blues')
    plt.show()
    
    #cv2.imshow('Lena',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
 
 
if __name__=="__main__":
    main()
    
