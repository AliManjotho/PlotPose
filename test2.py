import cv2
import numpy as np
from matplotlib import pyplot as plt
from helper import *

img1 = np.ones((480,480,3))
img2 = np.ones((480,480,3)) * 0.95
img3 = np.ones((480,480,3)) * 0.90

cx = 240
cy = 240
cz = 240

x1 = cx
y1 = cy
z1 = cz

x2 = 0
y2 = 0
z2 = 0

l = 100

rx = 45
ry = 45
rz = 45

rx = np.deg2rad(-rx)
ry = np.deg2rad(ry)
rz = np.deg2rad(-rz)


x2 = x1 + int(l * np.cos(rz))
y2 = y1 + int(l * np.sin(rz))
z2 = z1

new_l = (x2 - x1)
x2 = x1 + int(new_l * np.cos(ry))
z2 = z1 + int(new_l * np.sin(ry))

new_l = (z2 - z1)
z2 = z1 + int(new_l * np.cos(rx))
y2 = y1 + int(new_l * np.sin(rx))


cv2.line(img1, (0,cy),(480,cy), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.line(img1, (cx,0),(cx,480), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.circle(img1, (cx, cy), l, (0.0, 0.0, 1.0), 1, lineType=cv2.LINE_AA)
cv2.circle(img1, (cx, cy), int(l/2), (0.0, 0.0, 1.0), 1, lineType=cv2.LINE_AA)
cv2.putText(img1, "Front View", (15,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), thickness=1, lineType=cv2.LINE_AA)
cv2.putText(img1, "X", (460,260), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), thickness=2, lineType=cv2.LINE_AA)
cv2.putText(img1, "Y", (220,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), thickness=2, lineType=cv2.LINE_AA)

cv2.line(img2, (0,cz),(480,cz), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.line(img2, (cx,0),(cx,480), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.circle(img2, (cx, cz), l, (0.0, 0.0, 1.0), 1, lineType=cv2.LINE_AA)
cv2.circle(img2, (cx, cz), int(l/2), (0.0, 0.0, 1.0), 1, lineType=cv2.LINE_AA)
cv2.putText(img2, "Top View", (15,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), thickness=1, lineType=cv2.LINE_AA)
cv2.putText(img2, "X", (460,260), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), thickness=2, lineType=cv2.LINE_AA)
cv2.putText(img2, "Z", (220,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), thickness=2, lineType=cv2.LINE_AA)

cv2.line(img3, (0,cy),(480,cy), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.line(img3, (cz,0),(cz,480), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.circle(img3, (cz, cy), l, (0.0, 0.0, 1.0), 1, lineType=cv2.LINE_AA)
cv2.circle(img3, (cz, cy), int(l/2), (0.0, 0.0, 1.0), 1, lineType=cv2.LINE_AA)
cv2.putText(img3, "Left View", (15,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), thickness=1, lineType=cv2.LINE_AA)
cv2.putText(img3, "Z", (460,260), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), thickness=2, lineType=cv2.LINE_AA)
cv2.putText(img3, "Y", (220,20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), thickness=2, lineType=cv2.LINE_AA)




cv2.line(img1, (x1,y1),(x2,y2), (0.0,0.0,0.0), 3, cv2.LINE_AA)
cv2.circle(img1, (x1, y1), 7, (1.0, 0.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)
cv2.circle(img1, (x2, y2), 7, (0.0, 1.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)


cv2.line(img2, (x1,480 - z1),(x2,480-z2), (0.0,0.0,0.0), 3, cv2.LINE_AA)
cv2.circle(img2, (x1, 480-z1), 7, (1.0, 0.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)
cv2.circle(img2, (x2, 480-z2), 7, (0.0, 1.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)


cv2.line(img3, (z1,y1),(z2,y2), (0.0,0.0,0.0), 3, cv2.LINE_AA)
cv2.circle(img3, (z1, y1), 7, (1.0, 0.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)
cv2.circle(img3, (z2, y2), 7, (0.0, 1.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)


img1 = cv2.hconcat([img1, img2])
img4 = cv2.hconcat([img3, np.ones((480,480,3))])
img1 = cv2.vconcat([img1, img4])
print(np.sqrt(np.power((x2-x1),2) + np.power((y2-y1),2)))


cv2.imshow('Image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()