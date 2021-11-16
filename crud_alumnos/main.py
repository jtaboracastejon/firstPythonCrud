import sys
from user_interface import separador, show_menu
from alumno import Alumno
separador()
print("CRUD de Alumnos V 0.0.1")
separador()

teclado = sys.stdin

while True:
  show_menu()
  opcion = teclado.readline().rstrip().lstrip().upper()
  if opcion == "Q":
    break
  elif opcion == "T":
    mi_alumno = Alumno()
    mi_alumno.cuenta = "1234"
    mi_alumno.correo = "algo@gmail.com"
    mi_alumno.nombre = "Javier Castejon"
    mi_alumno.telefono = "12345678"
    mi_alumno.genero = "Masculino"
    print(mi_alumno.obtener_formato_columna())
    separador()
