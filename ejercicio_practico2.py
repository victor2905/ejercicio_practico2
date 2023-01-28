print("************************")
print("Es par o impar")
print("************************")
numero = int(input("Ingrese número a verificar: "))
residuo = numero%2
if residuo == 0:
    print("El número: ",numero,"es par")
else:
    print("El número: ",numero,"es impar")
