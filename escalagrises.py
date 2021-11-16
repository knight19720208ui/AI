'''
Versión de consola: python 
Cambiar a una escala de grises una imagen
'''
import cv2 
  
image = cv2.imread('leo.png')  # drive:\\path\\file
cv2.imshow('El Original', image) 
cv2.waitKey() 
  
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
cv2.imshow('En escala grises', gray_image) 
cv2.waitKey(0)   
  
cv2.destroyAllWindows() 
