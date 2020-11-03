import numpy as np

w1 = 1000
h1 = 1000
w2 = 4000
h2 = 1000
fovh = 60.0
fovv = 49.5
hipDepth = 3000


def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hlen = len(hex)
    r = int(hex[0:2], 16) / 256
    g = int(hex[2:4], 16) / 256
    b = int(hex[4:6], 16) / 256
    return (b, g, r)

def getEndPoint(p1, lineLength, angle):
    angle = np.deg2rad(angle)
    x2 = lineLength * np.cos(angle)
    y2 = lineLength * np.sin(angle)
    return (int(p1[0] + x2), int(p1[1] + y2))

def getEndPoint(p1, bone):
    boneLength = bone[2]
    rx = np.deg2rad(bone[3])
    ry = np.deg2rad(bone[4])
    rz = np.deg2rad(bone[5])
    x2 = boneLength * np.cos(rz)
    y2 = boneLength * np.sin(rz)
    return [int(p1[0] + x2), int(p1[1] + y2), int(p1[2] + y2)]



def getJoints(bones):

    joints = [[0,0,0] for i in range(0,21)]

    joints[10] = [int(w1 * 2), int(h1 * 2), hipDepth]

    for bone in bones:
        parent = bone[0]
        child = bone[1]
        boneLength = bone[2]
        rx = np.deg2rad(bone[3])
        ry = np.deg2rad(bone[4])
        rz = np.deg2rad(bone[5])
        x1 = joints[parent][0]
        y1 = joints[parent][1]
        z1 = joints[parent][2]
        x2 = 0
        y2 = 0
        z2 = 0

        # X-Rotation
        z2 = int(z1 + boneLength * np.cos(rx))
        y2 = int(y1 + boneLength * np.sin(rx))

        # Y-Rotation
        x2 = int(x1 + boneLength * np.cos(ry))
        z2 = int(z1 + boneLength * np.sin(ry))


        # Z-Rotation
        x2 = int(x1 + boneLength * np.cos(rz))
        y2 = int(y1 + boneLength * np.sin(rz))


        joints[child] = [x2, y2, z2]

    return joints