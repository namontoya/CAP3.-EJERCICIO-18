#Capitulo 3. Ejercicio propuesto 18

codigo_empleado = input("Ingrese su código: ")
nombres = input("Ingrese su nombre: ")
horas_trabajadas_mes = int(input("Ingrese el número de horas trabajadas al mes: "))
valor_hora = int(input("Ingrese el valor por hora trabajada: "))
porcentaje_retencion = int(input("Ingrese el porcentaje de retención en la fuente: ")) / 100

print(f"El código es: {codigo_empleado}")
print(f"Su nombre es: {nombres}")
print(f"El salario bruto es: {horas_trabajadas_mes * valor_hora}")
print(f"El salario neto es: {(horas_trabajadas_mes * valor_hora) * (1- porcentaje_retencion)}")


