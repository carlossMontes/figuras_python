from io import open
from os import system
import time

archivo_texto = open("prueba_python.txt", "r")

texto = archivo_texto.readlines()
archivo_texto.close()

# Cantidad de lineas en el archivo
lineas = len(texto)

# Ciclo for para recorrer el archivo linea por linea
for i in range(1, lineas, 1):
    print(texto[i], end="")
    time.sleep(1)

# Limpia la terminal
system("clear")