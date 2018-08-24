def constructorMaquina():
  while(True):
    try:
      mantisa = int(input())
      if(mantisa <= 0 or mantisa >= 14):
        print("numero incorrecto: este debe ser mayor que 0 y menor que 14")
      else:
        return mantisa
    except ValueError:
      print("ingrese un numero")
    
def epsilonMaquina(TamañoMantisa):
  return 2**(TamañoMantisa*-1)

def numeroMaquina(Decimal):
  return True


if __name__ == "__main__":
  print("Hola bienvenido a maquinaton 16 bits.\n")
  print("Esta maquina consta de 16 bits, los dos primeros seran los signos de la mantisa")
  print("y el exponente respectivamente, los siguientes bits seran para la mantiza y el exponente,") 
  print("ambos deberan ser mayores que 0 y menores que 14.\n")
  input()

  print("Ingresa un numero para asignarle a la mantisa, el numero restante se le asignara al exponente")
  mantisa = constructorMaquina()
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
  print("Exponente: ", 14-(mantisa) ," bits\n")
  input()

  while(True):
    try:
      print("Seleccione que hacer con maquinaton: ")
      print("seleccione ingresando en la consola el numero deseado, ejemplo 1")
      print("1. El numero positivo mas grande (overflow)(En decimal)")
      print("2. El epsilon de la maquina (En decimal)")
      print("3. El numero positivos mas pequeno(underflow)(En decimal)")
      print("4. El numero maquina correspondiente a un numero decimal dado por el usuario")
      print("5. El numero decimal correspondiente a un numero maquina dado por el usuario")
      print("6. Cambiar maquina")
      print("0. Salir")
      choice = int(input())
      if(choice>=0 and choice<= 6):
        if(choice == 1):
          print(choice)
          #llamar funcion correspondiente
          input()
        elif(choice == 2):
          print("El epsilon de esta maquina es", epsilonMaquina(mantisa))
          input()
        elif(choice == 3):
          print(choice)
          #llamar funcion correspondiente
          input()
        elif(choice == 4):
          print(choice)
          #llamar funcion correspondiente
          input()
        elif(choice == 5):
          print(choice)
          #llamar funcion correspondiente
          input()
        elif(choice == 6):
          print(choice)
          #llamar funcion correspondiente
          input()
        elif(choice == 0):
          break
      else:
        print("ingrese un numero valido")
    except ValueError:
      print("ingrese un numero")
    