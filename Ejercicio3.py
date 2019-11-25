#a) Usando ciclo for recorra la lista imprimiendo cada uno de sus elementos. valor 0.3
#b) Usando ciclo while recorra la lista imprimiendo cada uno de sus elementos


numero=[1,2,3,4,5,6,7,8,9,10]
print("For")
for i in range(len(numero)):
    print(numero[i],end='|')

print()


print("While")

i=0
while  i <(len(numero)):
    print(numero[i],end='|')
    i=i+1



