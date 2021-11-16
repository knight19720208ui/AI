import cv2
  
src = cv2.imread('leo.png', cv2.IMREAD_UNCHANGED)
 
#Porcentaje en el que se redimensiona la imagen
scale_percent = 50
 
#calcular el 50 por ciento de las dimensiones originales
#ancho = src.shape[1] 
#alto = src.shape[0] 

width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
 
# dsize
dsize = (width, height)
 
# cambiar el tamaño de la image
output = cv2.resize(src, dsize)
 
cv2.imwrite('leo_50p.png',output) 
