import cv2
import os
import imutils
#pip install imutils
#path_python.exe -m pip install --upgrade pip

personName = 'Pablo'
dataPath = 'imagenes' #Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName
numCamara = 1
if not os.path.exists(personPath):
	print('Carpeta creada: ',personPath)
	os.makedirs(personPath)
try:
	cap = cv2.VideoCapture(numCamara,cv2.CAP_DSHOW)  # 0, 1 son los índices de la cámara
		#cap = cv2.VideoCapture('Video.mp4')
except Exception as error:
	print('Error con algo de la cámara ' + str(error))
'''
# Cuando estamos en colab o jupyter
!wget --no-check-certificate \
    https://raw.githubusercontent.com/computationalcore/introduction-to-opencv/master/assets/haarcascade_frontalface_default.xml \
    -O haarcascade_frontalface_default.xml
'''
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while True:
	ret, frame = cap.read()
	if ret == False: break
	frame =  imutils.resize(frame, width=640)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = frame.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
		cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
		count = count + 1
	cv2.imshow('frame',frame)

	k =  cv2.waitKey(1)
	if k == 27 or count >= 300:
		break

cap.release()
cv2.destroyAllWindows()