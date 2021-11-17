def show_menu():
  print("M \t Mostrar los Registros de Alumnos")
  print("C \t Crear Nuevo Alumno")
  print("A \t Editar Alumno")
  print("B \t Borrar Alumno")
  print("Q \t Salir")
  separador()
  print("Escriba una opcion")

def show_registros(rows):
  separador()
  print("CUENTA\tNOMBRE\tTELEFONO\tGENERO\tCORREO")
  for row in rows:
    print(row[0] + "\t" + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[4])
  separador()

def separador():
  print("="*60)