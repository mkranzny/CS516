print("hello world")
print("BlahBlah")

import cv2
import numpy as np

camera = cv2.VideoCapture(0)
for i in range(2):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
del(camera)
