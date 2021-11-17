import cv2

laCamara = cv2.VideoCapture(0)

while (laCamara.isOpened()):
    ret, frame = laCamara.read()
    cv2.imshow('La Camara',frame)
    if (cv2.waitKey(1) == ord('s')):
        break

laCamara.release()
cv2.destroyAllWindows()
