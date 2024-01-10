
# This file is combination of Detection.py and PassImage1.py

import cv2
import numpy as np
import imutils
from imutils.object_detection import non_max_suppression
#import playsound as playsound

# Histogram Of Oriented Gradients Method
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detector(frame):
    # Here we are using Sliding Window concept
    rects, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.03)
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    c = 1
    for x, y, w, h, in pick:
        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y - 20), (w, y), (0, 0, 255), -1)
        cv2.putText(frame, f'P{c}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        c += 1

    cv2.putText(frame, f'Total Persons :{c - 1}', (20, 450), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 2)
    cv2.imshow('output', frame)
    return frame


# image detection code

img = cv2.imread('./inputs/ped2.jpg')
assert not isinstance(img,type(None)), 'image not found'
img = imutils.resize(img, width=800)
# img = cv2.resize(img,(1280,780))
print(img)
img = detector(img)


#playsound('beep-08b.mp3')

cv2.waitKey(0)
cv2.destroyAllWindows()