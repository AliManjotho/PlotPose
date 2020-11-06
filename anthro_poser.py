import cv2
from helper import *
from constants import *



# Parent, Child, boneLength, Rx, Ry, Rz
bones = [
         [10,11,124.21,0,0,180],  # L10
         [11,12,457.20,0,-60,-100],   # L11
         [12,13,444.50,0,-40,-90],      # L12
         [10,14,124.21,0,0,0],    # L13
         [14,15,457.20,0,-30,-100],    # L14
         [15,16,444.50,0,10,-90],  # L15
         [10,9,125.09,0,20,95],      # L9
         [9,8,250.19,0,20,95],       # L8
         [8,1,121.92,0,20,95],       # L7
         [1,0,190.50,0,20,95],       # L0
         [1,2,193.04,0,-15,190],     # L1
         [2,3,292.10,0,-15,190],     # L2
         [3,4,291.60,0,-25,190],    # L3
         [1,5,193.04,0,20,20],      # L4
         [5,6,292.10,0,20,20],        # L5
         [6,7,291.60,0,20,20],        # L6
         [0,17,81.69,0,0,125],     # L16
         [17,19,87.88,0,0,-130],    # L17
         [0,18,81.69,0,0,65],     # L18
         [18,20,87.88,0,0,-40]      # L19
        ]

joints = getJoints(bones)




frontImage = np.ones((h1,w1,3))
topImage = np.ones((h2,w2,3)) * 0.97
leftImage = np.ones((h3,w3,3)) * 0.93
rightImage = np.ones((h4,w4,3)) * 0.88


cv2.line(frontImage, (0, int(h1/2)),(w1, int(h1/2)), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.line(frontImage, (int(w1/2), 0),(int(w1/2), h1), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.putText(frontImage, "Front View", (20,60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=6, lineType=cv2.LINE_AA)
cv2.putText(frontImage, "Y", (int(w1/2) + 20 , 60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)
cv2.putText(frontImage, "X", (w1 - 60,int(h1/2) + 60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)

cv2.line(topImage, (0, h2 - 100),(w2, h2 - 100), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.line(topImage, (int(w2/2), 0),(int(w2/2), h2), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.putText(topImage, "Top View", (20,60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=6, lineType=cv2.LINE_AA)
cv2.putText(topImage, "Z", (int(w2/2) + 20 , 60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)
cv2.putText(topImage, "X", (w2 - 60,int(h2/2) + 60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)

cv2.line(leftImage, (0, int(h3/2)),(w3, int(h3/2)), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.line(leftImage, (100, 0),(100, h3), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.putText(leftImage, "Left View", (20,60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=6, lineType=cv2.LINE_AA)
cv2.putText(leftImage, "Y", (120 , 150), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)
cv2.putText(leftImage, "Z", (w3 - 60,int(h3/2) + 60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)

cv2.line(rightImage, (0, int(h4/2)),(w4, int(h4/2)), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.line(rightImage, (w4 - 100, 0),(w4 - 100, h4), (0.0,0.0,0.0), 1, cv2.LINE_AA)
cv2.putText(rightImage, "Right View", (20,60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=6, lineType=cv2.LINE_AA)
cv2.putText(rightImage, "Y", (w4 - 160, 150), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)
cv2.putText(rightImage, "-Z", (40, int(h4/2) + 60), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0), thickness=8, lineType=cv2.LINE_AA)





for b in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
    bone = bones[b]
    cv2.line(frontImage, (joints[bone[0]][0], joints[bone[0]][1]), (joints[bone[1]][0], joints[bone[1]][1]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)
    cv2.line(topImage, (joints[bone[0]][0], h2 - joints[bone[0]][2]), (joints[bone[1]][0], h2 - joints[bone[1]][2]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)
    cv2.line(leftImage, (joints[bone[0]][2], joints[bone[0]][1]), (joints[bone[1]][2], joints[bone[1]][1]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)
    cv2.line(rightImage, (w4 - joints[bone[0]][2], joints[bone[0]][1]), (w4 - joints[bone[1]][2], joints[bone[1]][1]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    joint = joints[i]
#for i, joint in enumerate(joints):
    cv2.circle(frontImage, (joint[0], joint[1]), 34, (0.5, 0.5, 0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(frontImage, (joint[0], joint[1]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)

    cv2.circle(topImage, (joint[0], h2 - joint[2]), 34, (0.5,0.5,0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(topImage, (joint[0], h2 - joint[2]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)

    cv2.circle(leftImage, (joint[2], joint[1]), 34, (0.5,0.5,0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(leftImage, (joint[2], joint[1]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)

    cv2.circle(rightImage, (w4 - joint[2], joint[1]), 34, (0.5,0.5,0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(rightImage, (w4 - joint[2], joint[1]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)



# 4
resizeFactor = 4
frontImage = cv2.resize(frontImage, (int(w1/resizeFactor), int(h1/resizeFactor)), interpolation = cv2.INTER_AREA)
topImage = cv2.resize(topImage, (int(w2/resizeFactor), int(h2/resizeFactor)), interpolation = cv2.INTER_AREA)
leftImage = cv2.resize(leftImage, (int(w3/resizeFactor), int(h3/resizeFactor)), interpolation = cv2.INTER_AREA)
rightImage = cv2.resize(rightImage, (int(w4/resizeFactor), int(h4/resizeFactor)), interpolation = cv2.INTER_AREA)





imgrow1 = cv2.hconcat([frontImage, topImage])
imgrow2 = cv2.hconcat([leftImage, rightImage])
img = cv2.vconcat([imgrow1, imgrow2])




xs = np.array([j[0] for j in joints])
ys = np.array([j[1] for j in joints])
zs = np.array([j[2] for j in joints])

sx = ( (sw/2) + np.rad2deg(np.arctan(xs/zs)) * sw / fovh ).astype(int)
sy = ( (sh/2) + np.rad2deg(np.arctan(ys/zs)) * sh / fovv ).astype(int)

imgScreen = np.ones((sh,sw,3))

for b in range(0, len(bones)):
    bone = bones[b]
    cv2.line(imgScreen, (sx[bone[0]], sy[bone[0]]), (sx[bone[1]], sy[bone[1]]), (0.5, 0.5, 0.5), 2, cv2.LINE_AA)

for i in range(0,len(sx)):
    cv2.circle(imgScreen, (sx[i], sy[i]), 6, (0.5, 0.5, 0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(imgScreen, (sx[i], sy[i]), 4, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)





cv2.imshow('Screen', imgScreen)
cv2.imshow('Pose',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


for j in joints:
    j[0] = j[0] - int(w1 / 2)
    j[1] = j[1] - int(h1 / 2)

for j in joints:
    print(j[0])
print("\n\n")
for j in joints:
    print(j[1])
print("\n\n")
for j in joints:
    print(j[2])
print("\n\n")


for x in sx:
    print(x)
print("\n\n")
for y in sy:
    print(y)

