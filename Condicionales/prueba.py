impuestos = 50000
ventas = 90000

if impuestos > 50000:
    if ventas - impuestos < 0:
        print("Estamos casi en bancarrota")
    elif ventas - impuestos >= 70000:
        print("Vas bien")
else:
    print("Tu negocio ha fracasado")
