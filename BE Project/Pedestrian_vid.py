
import cv2

cap = cv2.VideoCapture('./inputs/ped3.mp4')


while cap.isOpened():

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    diff = cv2.absdiff(frame1,frame2)
    g = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)      #creating gray scale image
    b = cv2.GaussianBlur(g, (5,5) ,0)
    _, thresh = cv2.threshold(b, 20, 255, cv2.THRESH_BINARY)
    dil = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dil, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)    #to draw contours
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1000:
                continue

        cv2.rectangle(frame1, (x,y), (x+w , y+h), (0,255,0), 2)
        cv2.putText(frame1, "Status: {}".format("Detected"), (10,20),cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255),3)

    cv2.imshow("Project", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()



    if cv2.waitKey(40) == 30:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.release()


