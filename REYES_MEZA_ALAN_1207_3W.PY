print(" ")
print("REYES MEZA ALAN EDUARDO 1207 : 3W")
print(" ")

#DE LECTURA1
#Abrir un archivo en el servidor
#Supongamos que tenemos el siguiente archivo, ubicado en la misma carpeta que Python:

#archivo de demostración.txt
#Hello! Welcome to demofile.txt
#This file is for testing purposes.
#Good Luck!


#Para abrir el archivo, utilice la función incorporada open().
#Para abrir el archivo, utilice la función incorporada open().
#La open()función devuelve un objeto de archivo, que tiene un read()método para leer el contenido del archivo:
#Ejemplo
#Obtenga su propio servidor Python

f = open("alumnos.txt", "r")
print(f.read())

print(" ")
#Si el archivo se encuentra en una ubicación diferente, deberá especificar la ruta del archivo, de esta manera:
#Ejemplo
#Abrir un archivo en una ubicación diferente:
import os

# Intentar abrir el archivo en una ubicación específica
try:
    with open(r"D:\myfiles\welcome.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no se encontró en la ubicación especificada.")
#Leer solo partes del archivo
#De forma predeterminada, el read()método devuelve el texto completo, pero también puedes especificar cuántos caracteres quieres devolver:
#Ejemplo
#Devuelve los 5 primeros caracteres del archivo:
f = open("alumnos.txt", "r")
print(f.read())
print(" ")

#ESCRITURA
#Escritura de archivos en Python
#❮ AnteriorPróximo ❯Escribir en un archivo existente
#Para escribir en un archivo existente, debe agregar un parámetro a la open()función:
#"a"- Anexar - se agregará al final del archivo
#"w"- Escribir: sobrescribirá cualquier contenido existente

#Ejemplo:
#Abra el archivo "demofile2.txt" y agregue contenido al archivo:
f = open("alumnos.txt", "w")
f.write("Now the file has more content!")
print(" ")
f.close()
#open and read the file after the appending:
f = open("alumnos.txt", "r")
print(f.read())
print(" ")
#Ejemplo
#Abra el archivo "demofile3.txt" y sobrescriba el contenido:
f = open("alumnos.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
print(" ")
#open and read the file after the overwriting:
f = open("alumnos.txt", "r")
print(f.read())
print(" ")

#ELIMINAR ARCHIVO

#liminar archivo de Python
#❮ AnteriorPróximo ❯Eliminar un archivo
#Para eliminar un archivo, debes importar el módulo del sistema operativo y ejecutar su os.remove()función:
#Ejemplo
#Eliminar el archivo "demofile.txt":
import os
try:
    with open("alumnos.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")

# Escribir en archivo
with open("alumnos.txt", "a") as f:
    f.write("Ahora el archivo tiene más contenido!\n")

# Leer después de añadir contenido
with open("alumnos.txt", "r") as f:
    print(f.read())

# Sobrescribir archivo
with open("alumnos.txt", "w") as f:
    f.write("He eliminado el contenido\n")

# Leer después de sobrescribir
with open("alumnos.txt", "r") as f:
    print(f.read())

# Eliminar archivo
try:
    if os.path.exists("alumnos.txt"):
        #os.remove("alumnos.txt")
        print("El archivo ha sido eliminado.")
    else:
        print("El archivo no existe.")
except PermissionError:
    print("No se puede eliminar el archivo porque está en uso.")
print(" ")

#Comprobar si el archivo existe:
#Para evitar obtener un error, es posible que desees verificar si el archivo existe antes de intentar eliminarlo:
#Ejemplo
#Comprueba si el archivo existe  elimínalo:
import os
if os.path.exists("myfolder"):
    print("La carpeta 'myfolder' existe.")
else:
    print("La carpeta 'myfolder' no existe.")

print(" ")
#Eliminar carpeta
#Para eliminar una carpeta entera, utilice el os.rmdir()método:
#Ejemplo
#Eliminar la carpeta "myfolder":

