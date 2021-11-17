import cv2

elVideo = cv2.VideoCapture('leo.avi')  # ruta al video, por omisión en el mismo directorio que este script

while (elVideo.isOpened()):
    ret, frame = elVideo.read()
    if (ret == True):
        cv2.imshow("gato0", frame)
        if (cv2.waitKey(30) == ord('s')):
            break
    else:
        break

elVideo.release()
cv2.destroyAllWindows()
