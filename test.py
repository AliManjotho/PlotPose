import cv2
import numpy as np
from matplotlib import pyplot as plt
from helper import *
from PIL import ImageColor

w1 = 1000
h1 = 1000
w2 = 4000
h2 = 1000
fovh = 60.0
fovv = 49.5
hipDepth = 3000


colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ff0000', '#000000']

# Parent, Child, boneLength, Rx, Ry, Rz
bones = [
         [10,11,124.21,0,0,195], # L10
         [11,12,457.20,0,-10,110], # L11
         [12,13,444.50,0,-10,95],  # L12
         [10,14,124.21,0,0,15],  # L13
         [14,15,457.20,0,0,85],  # L14
         [15,16,444.50,0,0,90],  # L15
         [10,9,125.09,0,0,-80],  # L9
         [9,8,250.19,0,0,-80],   # L8
         [8,1,121.92,0,0,-80],   # L7
         [1,0,190.50,0,0,-70],   # L0
         [1,2,193.04,0,0,195],   # L1
         [2,3,292.10,0,0,180],   # L2
         [3,4,291.60,0,0,220],   # L3
         [1,5,193.04,0,0,15],    # L4
         [5,6,292.10,0,0,50],    # L5
         [6,7,291.60,0,0,70],    # L6
         [0,17,81.69,0,0,-100],  # L16
         [17,19,87.88,0,0,155],  # L17
         [0,18,81.69,0,0,-40],   # L18
         [18,20,87.88,0,0,65]    # L19
        ]

joints = getJoints(bones)





frontImage = np.ones((h1,w1,3))
leftImage = np.ones((h2,w2,3))

for b in bones:
    cv2.line(frontImage, (int(joints[b[0]][0]/4),int(joints[b[0]][1]/4)),(int(joints[b[1]][0]/4),int(joints[b[1]][1]/4)), (0.5,0.5,0.5), 3, cv2.LINE_AA)

for i, j in enumerate(joints):
    cv2.circle(frontImage, (int(j[0]/4),int(j[1]/4)), 7, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)



for i, j in enumerate(joints):
    cv2.circle(leftImage, (int(j[2]/4),int(j[1]/4)), 7, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)



cv2.imshow('Front View',frontImage)
cv2.imshow('Left View',leftImage)
cv2.waitKey(0)
cv2.destroyAllWindows()