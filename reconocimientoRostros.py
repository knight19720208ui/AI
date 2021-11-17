# 1. Prepara entorno
# pip install face_recognition opencv-python numpy

# 2. Entrenamiento
'''
Carga la imagen de entrenamiento
will_smith_image = face_recognition.load_image_file("will_smith.jpg")
# Codifica la cara de entrenamiento
will_smith_face_encoding = face_recognition.face_encodings(will_smith_image)[0]
 
# Crea un arreglo con las distintas caras codificadas
known_face_encodings = [
   will_smith_face_encoding
]
# Crea un arreglo de los nombres en orden de las caras codificadas
known_face_names = [
   "Will Smith",
]
'''
'''
Face recognition carga la imagen y la codifica, dando como resultado una vector de flotantes de 128 dimensiones. 
Este vector es único para cada cara y nos permitirá en un futuro reconocer esa cara en otras fotos.
'''

# 3. Seleccionar la fuente de imágenes
'''
#extraer imagenes de un video
video_capture = cv2.VideoCapture('Will.mp4')
 
#extraer imagenes de la webcam
video_capture = cv2.VideoCapture(0)
 
if (video_capture.isOpened()== False):
 print("Error opening video stream or file")
''' 

# 4. Detectar caras
'''
# Toma los fotogramas del capturador
   ret, frame = video_capture.read()
 
   # Redimensiona el fotograma a 1/4 de resolucion para mejor rendimiento
   small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
 
   # Convierte la imagen de BGR color a RGB
   rgb_small_frame = small_frame[:, :, ::-1]
   
   
   
# encuentra y codifica todas las caras existentes en el fotograma
face_locations = face_recognition.face_locations(rgb_small_frame)

# con “face_encoding”, generando otra vez un vector de 128 dimensiones, con el que al fin podremos comparar la cara entrenada anteriormente
face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
'''

# 5. Comparar caras
'''
for face_encoding in face_encodings:
           # compara las caras codificadas con las caras entrenadas
           matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
           name = "Unknown"
 
           # usa la distancia entre las caras para encontrar la mayor probabilidad de match
           face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
           best_match_index = np.argmin(face_distances)
           if matches[best_match_index]:
               name = known_face_names[best_match_index]
 
           face_names.append(name)
'''

# 6. Presentar los resultados
'''
for (top, right, bottom, left), name in zip(face_locations, face_names):
       # Escala nuevamente el fotograma a la resolucion original
       top *= 4
       right *= 4
       bottom *= 4
       left *= 4
 
       # Dibuja un rectangulo al rededor del rostro
       cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
 
       # Dibuja el nombre del rostro encontrado
       cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
       font = cv2.FONT_HERSHEY_DUPLEX
       cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
 
   # Muestra el resultado de la imagen
   cv2.imshow('Video', frame)
'''

### Ver más: https://github.com/ageitgey/face_recognition 
