cadena_1 = "casa,camino,mesa"
cadena_2 = "hola"

#Funcion upper(convierte a mayusculas)
resultado = cadena_1.upper()

#Funcion lower (convierte a minusculas)

minusculas = cadena_2.lower()

#Primer letra en mayusculas + lower

primer_letra_masyucula = cadena_1.capitalize()

#Buscando una cadena en otra cadena

busquda_find = cadena_1.find("S")

#Buscando una cadena en otra cadena (.index), si no hay coincidencias lanza excepcion

busqueda_index = cadena_1.index("e")

#si es numero devolvemos true, sino devolvemos false
es_numerico = cadena_1.isnumeric()

#si es alfanumerico devuelve true, sino false
es_alafanumerico = cadena_1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantida de veces que coincida
contar_coincidenciasn = cadena_1.count("e")

#contamos cuantos caracteres tiene una cadena

contar_caracteres = len(cadena_1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena_1.startswith("b")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena_1.endswith("eso")

#Reemplaza un pedazo de cadena dada por otro pedazo de cadena dada
cadena_nueva = cadena_1.replace(","," ")

#separar cadenas con la cadena que le pasemos 
cadena_separada = cadena_1.split(",")

print(cadena_separada[1])