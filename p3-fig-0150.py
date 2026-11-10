import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

## Zavala Medina | NC= 0150
print("Zavala Medina| NC= 0150")
print("UIII Act3 colocar puntos a una imagen en blanco y negro VA")

mi_imagen = cv2.imread("Michealjackson.jpg")
mi_imagen_rgb = cv2.cvtColor(mi_imagen, cv2.COLOR_BGR2RGB)

plt.imshow(mi_imagen_rgb)
plt.title("Micheal Jackson y Zavala Medina")
plt.show()

print("+-+- Puntos en la imagen -+-+")

plt.imshow(mi_imagen_rgb)
plt.title("Imagen con Puntos 0150")

x = [100, 100, 300]
y = [100, 400, 500]
plt.scatter(x, y, s=20, c="red")

plt.show()