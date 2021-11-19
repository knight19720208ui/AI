"""
Esten es un sencillo script que muestra el uso del clasificador Haar para la detección de rostros
Se hara uso de la libreria open-cv. Puedes descargar open-cv utilizando el siguiente comando:
pip install opencv-ptyhon
"""

import cv2 # Importamos la libreria "open-cv"

# Importamos los archivos del cual el clasificador aprende las caracteristicas de cientos de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

img = cv2.imread('caras.jpg') # Leemos la imagen con la cual trabajaremos 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detectamos los rostros que se encuentran en la imagen
num_faces = 0 # Esta variable aumentara con respecta al numero de rostros detectados
for (x,y,w,h) in faces: # Guardasmo las coordenas de los rostros en una tupla
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # Con cv2.rentagle dibujamos un rectangulo en los rostros encontrados
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray) # Detectamos los ojos que se encuentran en la imagen
    for (ex,ey,ew,eh) in eyes: # Guardamos las coordenadas de los ojos que se encuentran en la imagen
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) # Dibujamos un rectangulo de color verde en los ojos detectados
    num_faces = num_faces+1 # Incrementamos la variable "num_faces"

cv2.imshow('img',img) # Mostramos el resultado
print(num_faces) # Imprimimos en pantalla el numero de rostros detectados
cv2.waitKey(0)
cv2.destroyAllWindows()
