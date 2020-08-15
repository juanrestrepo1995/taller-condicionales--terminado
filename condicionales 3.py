'''3) En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $1000
¿Cual será la cantidad que pagara una persona por su compra?'''
compra=float(input("digite el valor de la compra "))
if(compra>1000):
    desc=compra*0.20
else:
    desc=0
total_pago=compra-desc
print(f"el valor a pagar con descuento es de: {total_pago}")