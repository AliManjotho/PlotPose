import cv2
import csv
import numpy as np


depthImage = cv2.imread('depth.jpg')
depthImage = cv2.cvtColor(depthImage, cv2.COLOR_BGR2GRAY)

with open("new_file.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(depthImage)


cv2.imshow('depth', depthImage)
cv2.waitKey(0)
cv2.destroyAllWindows()