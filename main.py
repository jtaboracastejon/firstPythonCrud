import csv
#Esto es un comentario en Python
print("Hello world")
str_message = "Hola mundo!"
print(str_message)
print("="*80)

#Bloque de control y ciclos

bol_es_tercera_edad = False
if bol_es_tercera_edad:
  print("Si es tercera edad")
else:
  print("No es de tercera edad")
print("="*80)

#Ciclos
for i in range(0,100,10):
  print(i)
#leer csv
pfizer_count=0
astrazeneca_count=0
with open("data/covid19.csv") as covidFile:
  lector_csv = csv.reader(covidFile,delimiter=",")
  for linea in lector_csv:
    if linea[4] == "PSF":
      pfizer_count += 1
    if linea[4] == "AZT":
      astrazeneca_count += 1
print(astrazeneca_count, pfizer_count)
