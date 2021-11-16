#Leer datos de la linea de comando
import sys

#print("Escriba su nombre: ")
entrada = sys.stdin
#print("Su respuesta es " + entrada.readline())
#print("="*40)
#print("Escriba su correo: ")
#print("Su respuesta es " + entrada.readline())

print("Ingrese el primer operador: ")
operador1 = float(entrada.readline().lstrip().rstrip())
print("Ingrese el segundo operador: ")
operador2 = float(entrada.readline().lstrip().rstrip())
print("Determine la operacion: ")
print("+ Sumar, - Restar, / Dividir, * Multiplicar")
operacion = str(entrada.readline().lstrip().rstrip())
print(operacion)
print("="*40)
# Tarea en clase
# Determinar si la operacion es dentro de lo establecido
# Realizar la operacion asignandola a un variable
# Mostrar el Resutlado con el siguiente formato:
# <operador1> <tipo_operacion> <operador2> = <resutlado>

if operacion == "+":
  resultado = operador1+operador2
elif operacion == "-":
  resultado = operador1-operador2
elif operacion == "/":
  if operador2 == 0:
    print("MathError")
    exit()
  else:
    resultado = operador1/operador2
elif operacion == "*":
  resultado = operador1*operador2
else :
  print("Operacion invalida")
  exit()

print("El resultado de: " + str(operador1) + " " +
      operacion + " " + str(operador2) + " = " + str(resultado))
print("="*40)



