import cv2
import os
from datetime import datetime


def findFood(nombre):
 nombres = {"berenjena", "fresa", "huevos", "leche", "manzana", "naranja", "platano", "pollo", "solomillo", "tomate"}
 nombres = list(nombres)
 nombres.sort()
 x = 0
 existe = True
 while (x < len(nombres)) and existe :
        if(nombre == nombres[x]):
            existe = False
            comparePicture(x,nombre)
        x+=1

def comparePicture(x,nombre):
 BasePictures = os.listdir('D:/APUNTES/Python/Alimentos')
 im = cv2.imread(BasePictures[x],cv2.IMREAD_GRAYSCALE)
 y = 0
 encontrado = False
 while y < len(BasePictures) and (encontrado == False):
  im2 = cv2.imread(BasePictures[y],cv2.IMREAD_GRAYSCALE)
  d1 = cv2.matchShapes(im, im2, cv2.CONTOURS_MATCH_I2, 0)  # compara ambas imagenes
  if d1 <= 0.01:  # si el numero es menor a 0.01 es el mismo objeto, normalmente no se llega a 0.01 de desviación al modificar longitud, anchura o cantidad en los objetos.
    encontrado = True
    fecha = datetime.now()
    guardarDatos(fecha,nombre)


def guardarDatos(fecha,nombre):
    archivo = open('D:/APUNTES/Python/lista.txt',"a")
    textoAGuardar = fecha.strftime("%d/%m/%Y,%H:%M") + "_" + nombre + " "
    archivo.write(textoAGuardar)