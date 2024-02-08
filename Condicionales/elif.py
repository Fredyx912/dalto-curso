ingreso_mensual = 50000
gasto_mensual = 51000   

#if anidados y else if(elif)

if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual < 0:  
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
                print("ESTAS BIENN")    
    else:
        print("gastas mucho, deberias ahorrar")    
elif ingreso_mensual >= 5000:
    print("estas bien en latam")

elif ingreso_mensual >= 2000:
    print("estas bien en Perú")

elif ingreso_mensual > 1000:
    print("estas bien en Argentina")
    
else:
    print("eres misio")
    
     