ingreso_mensual = 14000
gasto_mensual = 13999
if ingreso_mensual > 7000:
   if ingreso_mensual -  gasto_mensual < 0:
    print("estas en bancarrota")
   elif ingreso_mensual - gasto_mensual > 6000:
       print("Ahorras bien")
   else: 
       print("gastas mucho, deberias ahorrar")
elif ingreso_mensual > 3000:
    print("Estas bien en cualquier parte del mundo con ese sueldo")
elif ingreso_mensual > 1000:
    print("ganas bien en todo el mundo")
else:
    print("ganas muy poco")
    