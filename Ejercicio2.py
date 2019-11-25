#Cree una función que reciba el nombre de una persona como argumento y retorne el número de letras
#de tal nombre, luego haga el llamado a la función y guarde su valor de retorno en una variable e imprima
#ese valor por consola.


nombre=input("Ingrese su nombre: ")


def calcularCant(nombre):
    cont=0
    for i in range(len(nombre)):
        if nombre[i]!=" ":
            cont=cont+1
    return cont

calcular=calcularCant(nombre)
print(calcular)


