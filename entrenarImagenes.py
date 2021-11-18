import cv2
import os
import numpy as np

dataPath = 'imagenes' #Cambia a la ruta donde hayas almacenado Data
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
	personPath = dataPath + '/' + nameDir
	print('Leyendo las imágenes...')

	for fileName in os.listdir(personPath):
		print('Caras: ', nameDir + '/' + fileName)
		labels.append(label)
		facesData.append(cv2.imread(personPath+'/'+fileName,0))
		# Ver lo que se esta aprendiendo:
		image = cv2.imread(personPath+'/'+fileName,0)
		cv2.imshow('image',image)
		# eso fue lo que aprendio de
		cv2.waitKey(3)
	label = label + 1

#print('labels= ',labels)
#print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
#print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))

# Métodos para entrenar el reconocedor
#1. face_recognizer = cv2.face.EigenFaceRecognizer_create()
#2. face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenando el modelo obtenido
#face_recognizer.write('modeloEigenFace.xml')
#face_recognizer.write('modeloFisherFace.xml')
face_recognizer.write('modeloLBPHFace.xml')
print("¡Modelo almacenado!")