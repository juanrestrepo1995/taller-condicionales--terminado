'''2)Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su
promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.'''
calificacion1=float(input("digite su primer nota "))
calificacion2=float(input("digite la segunda nota "))
calificacion3=float(input("digite tu tercera nota "))
promedio=(calificacion1+calificacion2+calificacion3)/3
if(promedio>=70):
    print("alumno aprueba")
else:
    print("alumno reprobado")