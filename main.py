import cv2
import numpy as np
from matplotlib import pyplot as plt
from helper import *

w1 = 1000
h1 = 800
w2 = 4000
h2 = 800
fovh = 60.0
fovv = 49.5
hipDepth = 3000

joints = [[0,0,0] for i in range(0,21)]

# J1, J2, boneLength, Rx, Ry, Rz
bones = [[0,1,190.50,0,0,-70],   # L0
         [1,2,193.04,0,0,195],   # L1
         [2,3,292.10,0,0,180],   # L2
         [3,4,291.60,0,0,220],   # L3
         [1,5,193.04,0,0,15],     # L4
         [5,6,292.10,0,0,50],     # L5
         [6,7,291.60,0,0,70],     # L6
         [1,8,121.92,0,0,-80],   # L7
         [8,9,250.19,0,0,-80],   # L8
         [9,10,125.09,0,0,-80],  # L9
         [10,11,124.21,0,0,195], # L10
         [11,12,457.20,0,0,110],  # L11
         [12,13,444.50,0,0,95],  # L12
         [10,14,124.21,0,0,15],   # L13
         [14,15,457.20,0,0,85],  # L14
         [15,16,444.50,0,0,90],  # L15
         [0,17,81.69,0,0,-100],  # L16
         [17,19,87.88,0,0,155],  # L17
         [0,18,81.69,0,0,-40],   # L18
         [18,20,87.88,0,0,65]    # L19
        ]

# Z-Rotation

joints[10] = [int(w1*2),int(h1*2), hipDepth]

joints[11] = getEndPoint(joints[10], bones[10])
joints[12] = getEndPoint(joints[11], bones[11])
joints[13] = getEndPoint(joints[12], bones[12])
joints[14] = getEndPoint(joints[10], bones[13])
joints[15] = getEndPoint(joints[14], bones[14])
joints[16] = getEndPoint(joints[15], bones[15])
joints[9] = getEndPoint(joints[10], bones[9])
joints[8] = getEndPoint(joints[9], bones[8])
joints[1] = getEndPoint(joints[8], bones[7])
joints[2] = getEndPoint(joints[1], bones[1])
joints[3] = getEndPoint(joints[2], bones[2])
joints[4] = getEndPoint(joints[3], bones[3])
joints[5] = getEndPoint(joints[1], bones[4])
joints[6] = getEndPoint(joints[5], bones[5])
joints[7] = getEndPoint(joints[6], bones[6])
joints[0] = getEndPoint(joints[1], bones[0])
joints[17] = getEndPoint(joints[0], bones[16])
joints[18] = getEndPoint(joints[0], bones[18])
joints[19] = getEndPoint(joints[17], bones[17])
joints[20] = getEndPoint(joints[18], bones[19])





# X-Rotation

#j11 = getEndPoint(joints[10],bones[10][2], bones[10][3])
#joints[11] = [joints[11][0], j11[1], j11[0]]




frontImage = np.ones((h1,w1,3))
leftImage = np.ones((h2,w2,3))

for b in bones:
    cv2.line(frontImage, (int(joints[b[0]][0]/4),int(joints[b[0]][1]/4)),(int(joints[b[1]][0]/4),int(joints[b[1]][1]/4)), (0.5,0.5,0.5), 3, cv2.LINE_AA)

for j in joints:
    cv2.circle(frontImage, (int(j[0]/4),int(j[1]/4)), 7, (1.0, 0.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)



for j in joints:
    cv2.circle(leftImage, (int(j[2]/4),int(j[1]/4)), 7, (1.0, 0.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)



cv2.imshow('Front View',frontImage)
cv2.imshow('Left View',leftImage)
cv2.waitKey(0)
cv2.destroyAllWindows()






# X = [0, 0, -193.04, -485.14, -776.74, 193.04, 485.14, 776.74, 0, 0, 0, -124.21, -124.21, -124.21, 124.21, 124.21, 124.21, -40.845, 40.845, -102.98, 102.98]
#
# Y = [-687.70, -497.20, -497.20, -497.20, -497.20, -497.20, -497.20, -497.20, -375.28, -125.09, 0, 0, 457.20, 901.70, 0, 457.20, 901.70, -758.44, -758.44, -700.68, -696.30]
#
# Z = [2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
#
# ZAnth = [190.50, 193.04, 292.10, 291.60, 193.04,
#          292.10, 291.60, 121.92, 250.19, 125.09,
#          124.21, 457.20, 444.50, 124.21, 457.20,
#          444.50, 81.69, 87.88, 81.69,87.88]
# joints = [(0,1), (1,2), (2,3), (3,4), (1,5), (5,6),(6,7),(1,8), (8,9), (9,10), (10,11), (11,12), (12,13), (10,14), (14,15), (15,16), (0,17), (0,18), (17,19), (18,20)]
#
# X = np.array(X)
# Y = np.array(Y)
# Z = np.array(Z)
# ZAnth = np.array(ZAnth)
#
# x = (w/2) + (np.rad2deg(np.arctan(X/Z)) * w / fovh)
# y = (h/2) + (np.rad2deg(np.arctan(Y/Z)) * h / fovv)
#
#
# img = np.ones((h,w,3))

#for j in joints:
#    cv2.line(img, (int(x[j[0]]), int(y[j[0]])), (int(x[j[1]]), int(y[j[1]])), (0.0, 0.0, 0.0), 2, lineType=cv2.LINE_AA)

# for i in range(0, 20+1):
#     cv2.circle(img, (int(x[i]), int(y[i])), 7, (1.0, 0.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)





# padding = 50
# xmin = np.min(X) - padding
# ymin = np.min(Y) - padding
# xmax = np.max(X) + padding
# ymax = np.max(Y) + padding
#
# x = (X - xmin)/2
# y = (Y - ymin)/2
#
# img = np.ones((int(np.max(y))+int(padding/2),int(np.max(x))+int(padding/2),3))
#
# for j in joints:
#     cv2.line(img, (int(x[j[0]]), int(y[j[0]])), (int(x[j[1]]), int(y[j[1]])), (0.0, 0.0, 0.0), 2, lineType=cv2.LINE_AA)
#
# for i in range(0, 20+1):
#     cv2.circle(img, (int(x[i]), int(y[i])), 7, (1.0, 0.0, 0.0), cv2.FILLED, lineType=cv2.LINE_AA)

