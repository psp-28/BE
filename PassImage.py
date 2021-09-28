import cv2
import imutils
from Detection import detector
from playsound import playsound

img = cv2.imread('img1.jpg')
img = imutils.resize(img, width=800)
# img = cv2.resize(img,(1280,780))
print(img)
img = detector(img)


playsound('beep-08b.mp3')

cv2.waitKey(0)
cv2.destroyAllWindows()
