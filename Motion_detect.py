# Using img subtraction

import cv2
import numpy as np

def diffimg(a,b,c):
    t0 = cv2.absdiff(b,a)
    t1 = cv2.absdiff(c,b)
    t3 = cv2.bitwise_and(t0,t1)
    return t3

cap = cv2.VideoCapture(0)

writer = cv2.VideoWriter('Vid.avi',cv2.VideoWriter_fourcc(*'XVID'),20,(640,480))


t = cap.read()[1]
tp = cap.read()[1]
tpp = cap.read()[1]


t = cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
tp = cv2.cvtColor(tp,cv2.COLOR_BGR2GRAY)
tpp = cv2.cvtColor(tpp,cv2.COLOR_BGR2GRAY)

while True:

    img = diffimg(t,tp,tpp)
    cv2.imshow('Motion Detect',img)

    writer.write(img)
    res,img = cap.read()
    t = tp
    tp = tpp
    tpp = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(10)
    if k&0xff is 27:
        cv2.destroyAllWindows()
        cap.release()
        writer.release()
        break
print('GoodBye World!')