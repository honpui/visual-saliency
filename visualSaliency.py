import cv2
import numpy

def vs(u):
    u1 = cv2.cvtColor(u,cv2.COLOR_BGR2GRAY)
    for i in range(0,8):
        u2 = cv2.pyrDown(u1,(5,5))
    for i in range(0,8):
        u1 = cv2.pyrUp(u2,(5,5))
    u1=cv2.resize(u1,(1000,700))
    u2=cv2.resize(u2,(1000,700))
    n1 = u1/u2
    d1 = u2/u1
    sol = numpy.minimum(n1,d1)
    sol*=200
    return sol

cap = cv2.VideoCapture(0)

while True:
    output = vs(cap.read()[1])
    cv2.imshow("Output",output)
    k = cv2.waitKey(20)
    if k&0xff is 27:
        cv2.destroyAllWindows()
        cap.release()
        break
    elif k&0xff is 112 :
        cv2.imwrite("OutputVisual_saliency.jpg",output)