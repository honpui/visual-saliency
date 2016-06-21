import cv2
import numpy as np
import sys

lp = cv2.imread('lp.jpg')
lowb = np.array([0, 0, 0])
uppb = np.array([35, 35, 35])
mask = cv2.inRange(lp, lowb, uppb)
_,contors,heirarcy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for i in range(0,len(contors),1):
    if 20000>cv2.contourArea(contors[i])>2000:
        M = cv2.moments(contors[i])
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print("Area : "+str(cv2.contourArea(contors[i]))+"  Centroid :"+str(cx)+" , "+str(cy))

        cv2.drawContours(lp,contors,i,(0,255,0),3)
        cv2.circle(lp,(cx,cy),2,(0,0,255),-1)
        cv2.imshow('OR', lp)
        cv2.waitKey(500)


#cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
