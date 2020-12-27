import cv2
import os

BasePictures = os.listdir('D:/APUNTES/Python/Alimentos')
#TestPictures = os.listdir()
im = cv2.imread(BasePictures[0], cv2.IMREAD_GRAYSCALE) #imagen a , aqui añadir la imagen que se clicka en la lista , cambiaria el BasePictures
im2 = cv2.imread('D:/APUNTES/Python/Alimentos/', cv2.IMREAD_GRAYSCALE) # imagen b , aqui se tiene que hacer un bucle iterando en las imagenes base que tenemos para comprobar que objeto es . Seria un while(!encontrado && quedanObjetos) se usa el matchShape
d2 = cv2.matchShapes(im,im2,cv2.CONTOURS_MATCH_I2,0)   # compara ambas imagenes
if d2 <= 0.01 : # si el numero es menor a 0.01 es el mismo objeto, normalmente no se llega a 0.01 de desviación al modificar longitud, anchura o cantidad en los objetos.
    encontrado = True
    #añadir el objeto con su nombre y la fecha en la lista de la otra UI
    cv2.imshow('berenjena',im)
    cv2.waitKey()