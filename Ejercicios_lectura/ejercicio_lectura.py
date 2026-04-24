"""
Crea un programa que:

Lea un archivo texto.txt
Muestre:
Número total de caracteres
Número de líneas
Primera línea
"""

with open("datos/quijote.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
count=len(contenido)

"""OPCIÓN CLÁSICA
import os
ruta = archivo.name
nombre = os.path.basename(ruta)
nombre_sin_ext = os.path.splitext(nombre)[0]
print(nombre_sin_ext,"tiene", count, "letras.")
"""

"""CON PATHLIB(Más moderna y recomendable)"""
from pathlib import Path
ruta = Path(archivo.name)
print(ruta.stem,"tiene",count,"letras")



#------------------------------------------------------------------

"""2. Contar palabra específica
Lee texto.txt
Cuenta cuántas veces aparece la palabra "amor"
Ignora mayúsculas/minúsculas

👉 Pista:

contenido.lower().count("amor")
"""
#Cuenta también subcadenas tipo "Amores"
love = contenido.lower().count("amor")
print("Hay",love,"palabras 'amor' o que contienen 'amor'")

#Sólo "amor"
import re

love = len(re.findall(r"\bamor\b", contenido.lower()))
#r -> raw string
#\b -> backspace
print("Hay",love,"palabras 'amor'")


#-------------------------------------------------------------------

"""3. Guardar líneas con una palabra
Lee texto.txt
Guarda en amor.txt solo las líneas que contienen "amor"
"""

#--------------------------------------------------------------------

"""NIVEL 2 — INTERMEDIO
4. Limpiar texto
Leer archivo
Reemplazar:
Saltos de línea por espacios
Eliminar dobles espacios
Guardar resultado en limpio.txt
"""

#------------------------------------------------------------------


  