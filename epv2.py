import numpy as np
import cv2
import detecta_objeto as do
import detecta_verde as dv

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    obj1 = cv2.imread("objeto1.jpg")
    obj2 = cv2.imread("objeto2.jpg")

    mask = dv.detV(frame)
    frame1 = do.detO(mask, obj1, obj2, frame)

    cv2.imshow("aperta 'p' para fechar", frame1)

    if cv2.waitKey(1)==ord('p'):
        break
cap.release()
cv2.destroyAllWindows()