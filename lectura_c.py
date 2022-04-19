from io import open
from os import system
import time

archivo_texto = open("letra_c.txt", "r")

texto = archivo_texto.readlines()
archivo_texto.close()

lineas = len(texto)

for i in range(0, lineas, 16):
    for k in range(0, 16, 1):
        print(texto[k + i], end="")
    time.sleep(1)
    system("clear")