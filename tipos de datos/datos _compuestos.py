#creando una lista (se pueden modificar)
lista = ["FERNANDO","PAN","AZUCAR",True, 1.85]

#creando una lista (no se pueden modificar)
tupla = ["FERNANDO","PAN","AZUCAR",True, 1.85]

#esto es valido
lista[2] = "HARINA"

#esto n es valido
#tupla[2] = "HARINA"  

#creando un conjunto (set) (no se acceden a los datos mediante indice, no se admiten duplicaods)
conjunto = {"FERNANDO","PAN","AZUCAR"}
conjunto = {"oaaaaa xdxd ", "pan","pan","pan"}

#print(conjunto[1]) = no se puede acceder al elemento
 
#creando un diccionarios
diccionario = {
    "nombre": "Fernando",
    "Edad" : "20",
    "Ciudad": "Lima",
    "Esta feliz?": True,
    "Datos_duplicado" : "Soy Fernando",
    "altura": 1.82 
        }

print(diccionario["nombre"])
print(diccionario["altura"] + 2)