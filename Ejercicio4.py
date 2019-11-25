cantPersonas=int(input("Ingrese la cantidad de personas a registrar"))

diccionario={}
i=0
while i<cantPersonas:
    print("Persona ",(i+1))
    documento=input("Ingrese el numero de documento")
    nombre=input("Ingrese el nombre ")
    edad=input("Ingrese la edad")
    estaura=input("Ingrese la estatura")
    diccionario[documento]={"id":documento,"nombre":nombre,"edad":edad,"estatura":estaura}
    print("Registro exitoso\n")
    i=i+1
print(diccionario)

menu="Consultar registro\n\n"
menu+="1. Si\n"
menu+="2. No\n\n"
menu+="Ingrese segun corresponda"
cant=int(input(menu))
print()

if cant==1:
        usuario=input("Ingrese su id")
        print("Su nombre es: ",diccionario[usuario]["nombre"])
        print("Su documento es: ",diccionario[usuario]["id"])
        print("Su edad es: ",diccionario[usuario]["edad"])
        print("Su estatura es: ",diccionario[usuario]["estatura"])

elif cant==2:
    print("Ha salido")    

