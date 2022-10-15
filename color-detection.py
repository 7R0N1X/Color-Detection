import cv2
import numpy as np

# DRAWING FUNCTION
def draw(mask, color, name):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)
        if area > 3000:
            M = cv2.moments(c)
            if M["m00"] == 0:
                M["m00"] = 1
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            cv2.circle(frame, (x, y), 7, color, -1)
            font = cv2.FONT_HERSHEY_SIMPLEX

            # COLOR VALIDATION
            if name == "Blue":
                cv2.putText(frame, "Blue: {},{}".format(x, y), (x + 10, y), font, 0.75, color, 1, cv2.LINE_AA,)
                newContours = cv2.convexHull(c)
                cv2.drawContours(frame, [newContours], 0, color, 3)
            
            if name == "Red":
                cv2.putText(frame, "Red: {},{}".format(x, y), (x + 10, y), font, 0.75, color, 1, cv2.LINE_AA,)
                newContours = cv2.convexHull(c)
                cv2.drawContours(frame, [newContours], 0, color, 3)

cap = cv2.VideoCapture(0)

# COLOR DECLARATION
lowRed1 = np.array([0, 100, 20], np.uint8)
highRed1 = np.array([8, 255, 255], np.uint8)
lowRed2 = np.array([175, 100, 20], np.uint8)
highRed2 = np.array([179, 255, 255], np.uint8)

lowBlue = np.array([100, 100, 20], np.uint8)
highBlue = np.array([125, 255, 255], np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(frameHSV, lowRed1, highRed1)
        maskRed2 = cv2.inRange(frameHSV, lowRed2, highRed2)
        maskRed = cv2.add(maskRed1, maskRed2)
        maskBlue = cv2.inRange(frameHSV, lowBlue, highBlue)

        draw(maskBlue, (255, 0, 0), "Blue")
        draw(maskRed, (0, 0, 255), "Red")
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break

cap.release()
cv2.destroyAllWindows()