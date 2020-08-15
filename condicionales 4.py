'''4) Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
Si trabaja 40 horas o menos se le paga $16 por hora
Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.'''
horastrab=int(input("digite las horas trabajadas "))
if (horastrab>40):
    horaex=horastrab-40
    sal_sem=horaex*20+40*16
else:
    sal_sem=horastrab*16
print(f"su salario semanal es de: {sal_sem}")