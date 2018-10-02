# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:39:35 2018

@author: HIMANSHU
"""
import cv2
import matplotlib.pyplot as plt


def main():
    
    imgpath="C:\\Users\\HIMANSHU\\Desktop\\OpenCV_Dataset\\standard_test_images\\lena_color_512.tif"
    img=cv2.imread(imgpath,3)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()




if __name__ =="__main__":
    main()