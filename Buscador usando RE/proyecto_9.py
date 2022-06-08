import datetime
import os
import re
import time
from pathlib import Path
import math

inicio = time.time()
# Datos
ruta='D:\\Cursos - Certificaciones\\Udemy\\Python TOTAL\\Dia 9\\Mi_Gran_Directorio'
patron = r'N\w{3}-\d{5}'
fecha = datetime.date.today()
dia, mes, anio = [fecha.day, fecha.month, fecha.year]

def programa():
    l_codigos=[]
    l_archivos=[]
    for carpeta, subcarpeta, archivo in os.walk(ruta):

        for file in archivo:

            archivo = open (Path(carpeta,file), 'r')
            transcrito = archivo.read()

            if re.search(patron, transcrito):
                coincidencia = re.search(patron, transcrito)
            else:
                coincidencia = ''

            if coincidencia != '':
                    l_codigos.append((coincidencia.group()))
                    l_archivos.append(file.title())
    return l_codigos, l_archivos

l_codigos, l_archivos = programa()

print('\nBienvenido al Buscador de Numeros de Serie')
print('-'*50)
print(f'Fecha de busqueda: {dia}/{mes}/{anio}')
print()
print ('ARCHIVO\t\t\tNO. DE SERIE')
print('-'*7+'\t\t\t'+'-'*12)
for i in range (len(l_archivos)):
    print(f'{l_archivos[i]}\t\t{l_codigos[i]}')
print()
print(f'Numeros encontrados: {len(l_codigos)}')
fin=time.time()
print(f'Duracion de la busqueda: {math.ceil(fin-inicio)} segundos')
print('-'*50)
