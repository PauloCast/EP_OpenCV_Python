import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    l = int(cap.get(3))
    h = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mingreen = np.array([20, 98, 0])
    maxgreen = np.array([95, 255, 189])

    mask = cv2.inRange(hsv, mingreen, maxgreen)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("aperta 'p' para fechar", result) 

    if cv2.waitKey(1)==ord('p'):
        break
    
cap.release()
cv2.destroyAllWindows()