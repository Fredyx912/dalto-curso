lista = ["AZUCAR", "PAN", "CARNE", "AGUA", "CAFE",2,True,False]
print(lista[3])

tupla = ("AZUCAR", "PAN", "CARNE", "AGUA", "CAFE",2,True,False)
print(tupla[5])

lista[4] = "POLLO"

print(lista[4])

conjunto = {"AZUCAR", "PAN", "CARNE", "AGUA", "CAFE",2,True,False}
conjunto = {"AZUCAR", "PAN"}

print(conjunto)

diccionario = {"DULCE": "AZUCAR",
 "BEBIDA": "AGUA",
 "COMIDA":"PAN",
 "PESO": 2    
}

print(diccionario["PESO"] + 2 )
print(diccionario["BEBIDA"])