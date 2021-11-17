import cv2

laWebCam = cv2.VideoCapture(0)
#objeto salidaGuardada, contiene los parámetros para crear el video
salidaGuardada = cv2.VideoWriter('laWebCamCapturada.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, (640,480))

while (True):
    ret, frame = laWebCam.read()
    cv2.imshow('frame',frame)
    #Usar write para GUARDAR el video
    salidaGuardada.write(frame)
    if (cv2.waitKey(1) == ord('s')):
        break

salidaGuardada.release()
laWebCam.release()
cv2.destroyAllWindows()
