import cv2
from helper import *
from constants import *



# Parent, Child, boneLength, Rx, Ry, Rz
bones = [
         [10,11,124.21,-90,-195,0],   # L10
         [11,12,457.20,-35,-100,0],   # L11
         [12,13,444.50,-110,-110,0],  # L12
         [10,14,124.21,-90,-15,0],    # L13
         [14,15,457.20,-80,-80,0],    # L14
         [15,16,444.50,-100,-100,0],  # L15
         [10,9,125.09,90,-75,0],      # L9
         [9,8,250.19,90,-75,0],       # L8
         [8,1,121.92,90,-75,0],       # L7
         [1,0,190.50,90,-75,0],       # L0
         [1,2,193.04,-90,-195,0],     # L1
         [2,3,292.10,-50,-200,0],     # L2
         [3,4,291.60,-130,-265,0],    # L3
         [1,5,193.04,-90,-15,0],      # L4
         [5,6,292.10,85,35,0],        # L5
         [6,7,291.60,85,50,0],        # L6
         [0,17,81.69,-90,-240,0],     # L16
         [17,19,87.88,-90,-150,0],    # L17
         [0,18,81.69,-90,-330,0],     # L18
         [18,20,87.88,-90,-60,0]      # L19
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

cv2.line(topImage, (0, int(h2/2)),(w2, int(h2/2)), (0.0,0.0,0.0), 1, cv2.LINE_AA)
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





for bone in bones:
    cv2.line(frontImage, (joints[bone[0]][0], joints[bone[0]][1]), (joints[bone[1]][0], joints[bone[1]][1]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)
    cv2.line(topImage, (joints[bone[0]][0], h2 - joints[bone[0]][2]), (joints[bone[1]][0], h2 - joints[bone[1]][2]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)
    cv2.line(leftImage, (joints[bone[0]][2], joints[bone[0]][1]), (joints[bone[1]][2], joints[bone[1]][1]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)
    cv2.line(rightImage, (w4 - joints[bone[0]][2], joints[bone[0]][1]), (w4 - joints[bone[1]][2], joints[bone[1]][1]), (0.5, 0.5, 0.5), 12, cv2.LINE_AA)

for i, joint in enumerate(joints):
    cv2.circle(frontImage, (joint[0], joint[1]), 34, (0.5, 0.5, 0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(frontImage, (joint[0], joint[1]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)

    cv2.circle(topImage, (joint[0], h2 - joint[2]), 34, (0.5,0.5,0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(topImage, (joint[0], h2 - joint[2]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)

    cv2.circle(leftImage, (joint[2], joint[1]), 34, (0.5,0.5,0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(leftImage, (joint[2], joint[1]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)

    cv2.circle(rightImage, (w4 - joint[2], joint[1]), 34, (0.5,0.5,0.5), cv2.FILLED, lineType=cv2.LINE_AA)
    cv2.circle(rightImage, (w4 - joint[2], joint[1]), 25, hex_to_rgb(colors[i]), cv2.FILLED, lineType=cv2.LINE_AA)




resizeFactor = 10
frontImage = cv2.resize(frontImage, (int(w1/resizeFactor), int(h1/resizeFactor)), interpolation = cv2.INTER_AREA)
topImage = cv2.resize(topImage, (int(w2/resizeFactor), int(h2/resizeFactor)), interpolation = cv2.INTER_AREA)
leftImage = cv2.resize(leftImage, (int(w3/resizeFactor), int(h3/resizeFactor)), interpolation = cv2.INTER_AREA)
rightImage = cv2.resize(rightImage, (int(w4/resizeFactor), int(h4/resizeFactor)), interpolation = cv2.INTER_AREA)





imgrow1 = cv2.hconcat([frontImage, topImage])
imgrow2 = cv2.hconcat([leftImage, rightImage])
img = cv2.vconcat([imgrow1, imgrow2])




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
