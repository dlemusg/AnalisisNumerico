def menu():
  return True
  
def constructorMaquina(mantisa):
  if(mantisa <= 0 or mantisa >= 14):
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
  Memory = [16]
  DSMantisa = 0 #Direccion del signo de la mantisa
  DSExp = 1 #Direccion del signo del exponente
  Dmantisa = 2 #Direccion donde comienza la mantisa
  mantisa = mantisa - 1 # Tamaño de la mantisa
  Dexp = 2 + mantisa #Direccion donde comienza el exp ( este termina en la casilla 0)

  print("Esta maquina esta construida de esta forma:")
  print("Signo mantisa: 1 bit")
  print("Signo exponente: 1 bit")
  print("Mantisa:", mantisa+1," bits (el bit mas significativo es un bit implicito)")
  print("Exponente: ", 14-(mantisa) ," bits")

    