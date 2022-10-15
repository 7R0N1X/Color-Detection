import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lowRed1 = np.array([0, 100, 20], np.uint8)
highRed1 = np.array([8, 255, 255], np.uint8)

lowRed2 = np.array([175, 100, 20], np.uint8)
highRed2 = np.array([179, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, lowRed1, highRed1)
        maskRed2 = cv2.inRange(frameHSV, lowRed2, highRed2)
        maskRed = cv2.add(maskRed1, maskRed2)

        maskRedvis = cv2.bitwise_and(frame, frame, mask=maskRed)
        cv2.imshow("maskRedvis", maskRedvis)

        cv2.imshow("maskRed", maskRed)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break

cap.release()
cv2.destroyAllWindows()
