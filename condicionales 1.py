'''1) Un hombre desea saber cuanto dinero se genera por concepto de intereses sobre
la cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses
siempre y cuando estos excedan a $7000, y en ese caso desea saber cuanto dinero tendrá
finalmente en su cuenta.'''
porc_inte=float(input(f"digite el porcentaje del interes "))
capital=float(input(f"digite el capital que desea invertir "))
intere = capital * porc_inte
if(intere > 7000):
    capitalfin = capital + intere
    print(f"su capital final es de:{capitalfin}")
