#mi-primera-calculadora
def suma(num1,num2):
  print("suma :")
  return num1+num2

def resta(num1,num2):
   print("resta :")
   return num1-num2

a=float(input("ingrese el primer valor :"))
b=float(input("ingrese el segundo valor :"))

imp_suma=suma(a,b)
print(imp_suma)
imp_resta=resta(a,b)
print(imp_resta) 
