num = 1.79769313
divisor = 0.0001
d = 1.7
cont = 0;
print("se inicial con el número " + str(num) + " y se divide por 0.0001 para ir aumentando hasta llegar al numero que phyton representa como infinito")
while num != float('inf'):
  d = num
  num = num/divisor
  cont = cont + 1

print("El numero mayor almacenado por la máquina es " + str(d));
print("El número de iteraciones para hayar el mayor numero fue " + str(cont));
