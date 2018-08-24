def menu():
  return True
  
def constructorMaquina(mantisa):
  if(mantisa < 0 or mantisa >= 14):
    print("numero incorrecto: este debe ser mayor que 0 y menor que 14")
    return False
  else:
    return True

if __name__ == "__main__":
  print("Hola bienvenido a maquinaton 16 bits.\n")
  print("Esta maquina consta de 16 bits, los dos primeros seran los signos de la mantisa")
  print("y el exponente respectivamente, los siguientes bits seran para la mantiza y el exponente,") 
  print("ambos deberan ser mayores que 0 y menores que 14.\n")

  print("Ingresa un numero para asignarle a la mantisa, el numero restante se le asignara al exponente")
  while(True):
    mantisa = int(input())
    if(constructorMaquina(mantisa)):
      break
    