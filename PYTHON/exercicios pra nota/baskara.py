from math import pow

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

Delta = b*b - 4*a*c


if Delta < 0:
 print("esta equação não possui raízes reais")
elif Delta == 0:
  print("a raiz desta equação é X")
  raiz = (-b + pow(Delta,1/2))/2*a
  print(f"A raiz é: x = {raiz}")
else:
   print("a raiz dupla desta equação é X")
   raiz1 = (-b + pow(Delta,1/2))/2*a
   raiz2 = (-b - pow(Delta,1/2))/2*a
   print(f"x1 = {raiz1:.2f}, x2 = {raiz2:.2f}")
