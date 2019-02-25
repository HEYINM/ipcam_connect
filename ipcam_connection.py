#-*-coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture('http://192.168.43.161:29444/videostream.cgi?user=admin&pwd=88888888')
#cap = cv2.VideoCapture('rstp://admin:{88888888}@192.168.43.161:29444/tcp/av0_0')

print('ffffff')

while(True):
    #Capture frame-by-frame
    ret,frame = cap.read()
    #print frame.shape
    print('why')

    if(ret):
        #if cam read is successfull
        #Our operations on the frame come here
        #display the result frame
        cv2.imshow('frame',frame)
        print('hehehe')

        #this should be called always, frame or not.
        if cv2.waitKey(1)&0xFF==ord('q'):
            break
        #When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
