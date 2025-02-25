import numpy as np
from constants import *

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    r = int(hex[0:2], 16) / 256
    g = int(hex[2:4], 16) / 256
    b = int(hex[4:6], 16) / 256
    return (b, g, r)




def getJoints(bones):

    joints = [[0,0,0] for i in range(0,21)]

    joints[10] = [int(w1 / 2), int(h1 / 2), hipDepth]
    #joints[10] = [0, 0, hipDepth]

    for bone in bones:
        parent = bone[0]
        child = bone[1]
        boneLength = bone[2]
        rx = np.deg2rad(-bone[3])
        ry = np.deg2rad(bone[4])
        rz = np.deg2rad(-bone[5])
        x1 = joints[parent][0]
        y1 = joints[parent][1]
        z1 = joints[parent][2]

        x2 = x1 + boneLength
        y2 = y1
        z2 = z1

        l = (z2 - z1)
        z2 = z1 + int(l * np.cos(rx))
        y2 = y1 + int(l * np.sin(rx))

        l = (x2 - x1)
        x2 = x1 + int(l * np.cos(ry))
        z2 = z1 + int(l * np.sin(ry))

        l = (x2 - x1)
        x2 = x1 + int(l * np.cos(rz))
        y2 = y1 + int(l * np.sin(rz))


        joints[child] = [x2, y2, z2]

    return joints