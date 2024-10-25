print(" ")
print("REYES MEZA ALAN EDUARDO 1207 : 3W")
print(" ")

archivo = open ("alumnos.txt", "r")  #abro mi archivo de texto para solo lectura
print (archivo.readable())

archivo.close()

import os
os.remove("alumnos.txt")


