# Cree una función que reciba como argumentos dos números y retorne el mayor de estos números,
#luego haga el llamado a la función y guarde su valor de retorno en una variable e imprima ese valor por
#consola. valor 1.5

def mayorNum(num1,num2):
    if num1>num2:
        numMayor=num1
    elif num2>num1:
        numMayor=num2
    return numMayor

num1=int(input("Ingrese un numero entero"))
num2=int(input("Ingrese un numero entero"))



print("\nDe los numeros ingresados {0} y {1}".format(num1,num2),"\n")

if num1>num2 or num2>num1:
    calcular=mayorNum(num1,num2)
    print("El numero mayor es: ",calcular)
else:
    print("Los numeros son iguales")

print()