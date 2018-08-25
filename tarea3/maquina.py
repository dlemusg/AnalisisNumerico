from decimal import Decimal  
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

def cpila(bin):
  pila = []
  cont = 0
  while(bin != 0):
    pila.append(bin % 2)
    bin = int(bin/10)
    cont = cont + 1
  return pila

def numeroMaquina(conv, Dexp):
  num = int(conv)
  decimal = conv - num
  maquina = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
  #signo de la mantisa
  if conv >= 0:
    maquina[0] = 1
  #signo del exponente
  if conv > 0 and conv < 1 :
    maquina[1] = 0
  else:
    maquina[1] = 1
  #parte entera de la mantisa
  if num < 0:
    num = num*-1
  mant1 = "{0:b}".format(num)
  mant2 = int(mant1)
  print("mant2", mant2)
  pila = cpila(mant2)

  if len(pila) > 0:  
    a = pila.pop() #se bota el bit mas significativo
  cont2 = 2
  tamp = len(pila)+2
  while(cont2 < tamp and cont2 != Dexp and len(pila)>0):
    maquina[cont2]=pila.pop()
    cont2 = cont2 + 1

  #decimal
  while cont2 != Dexp and decimal != 0 :
    decimal = decimal * 2
    if(decimal >= 1):
      maquina[cont2] = 1
      decimal = decimal -1
    else:
      maquina[cont2] = 0
    cont2 = cont2 + 1

  #exponente
  exp = "{0:b}".format(len(mant1))
  pila = cpila(int(exp))
  cont2 = Dexp
  while(cont2 < 16 and len(pila)>0):

    maquina[cont2]=pila.pop()
    cont2 = cont2 + 1
  
  print("El numero ", conv, " en numero maquina es: ", end = "")
  for i in maquina:
    print(i, end="")



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
      print("0. Salir")
      choice = int(input())
      if(choice>=0 and choice<= 5):
        if(choice == 1):
          #llamar funcion correspondiente
          input()
        elif(choice == 2):
          print("El epsilon de esta maquina es", epsilonMaquina(mantisa))
          input()
        elif(choice == 3):
          #llamar funcion correspondiente
          input("")
        elif(choice == 4):
          while(True):
            try:
              decimal = float(input("Ingrese un numero decimal para convertir a numero maquina: "))
              numeroMaquina(decimal,Dexp)
              break
            except ValueError:
              print("ingrese un numero valido ej: 2.5 (use . y no ,)")
          input()
        elif(choice == 5):
          #llamar funcion correspondiente
          input()
        elif(choice == 6):
          #llamar funcion correspondiente
          input()
        elif(choice == 0):
          break
      else:
        print("ingrese un numero valido")
    except ValueError:
      print("ingrese un numero")