# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:24:19 2018

@author: HIMANSHU
"""

import cv2

def main():
    cap=cv2.VideoCapture(0)
    while True:
      ret, frame=cap.read()
      cv2.imshow('frame',frame)
    
    
      if(cv2.waitKey(0) & 0xFF==orf('q')):
           break
        
        

    cap.release()
    cap.destroyAllWindows()

if __name__ =="__main__":
    main()