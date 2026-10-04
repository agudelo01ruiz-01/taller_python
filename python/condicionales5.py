#5.Elaborar un algoritmo que solicite el nombre de un empleado, las horas trabajadas durante el mes y el valor de cada hora.
#Las primeras 160 horas son horas normales y se pagan con la tarifa establecida.
#Las horas por encima de 160 son horas extra y se pagan al 125 % del valor de la hora normal.
#Validar que las horas trabajadas y el valor de la hora sean valores positivos.
#Calcular un descuento de salud y pensión equivalente al 8 % del salario total (bruto) y obtener el salario neto a pagar.
#Al finalizar, debe mostrar las horas normales, las horas extra, el pago por cada una, el salario total (bruto) y el salario neto después del descuento.

# Solicitar datos del empleado
nombre = input("Ingrese el nombre del empleado: ")

# Validar que las horas trabajadas sean un valor positivo
while True:
    horas_totales = float(input("Ingrese las horas trabajadas en el mes: "))
    if horas_totales > 0:
        break
    print("Error: Las horas deben ser un valor positivo. Intente de nuevo.")

# Validar que el valor de la hora sea un valor positivo
while True:
    valor_hora = float(input("Ingrese el valor de cada hora: "))
    if valor_hora > 0:
        break
    print("Error: El valor de la hora debe ser positivo. Intente de nuevo.")

# Calcular horas normales y extras usando condicionales
if horas_totales <= 160:
    horas_normales = horas_totales
    horas_extra = 0
else:
    horas_normales = 160
    horas_extra = horas_totales - 160

# Calcular pagos (las horas extra se pagan al 125%)
pago_normal = horas_normales * valor_hora
pago_extra = horas_extra * (valor_hora * 1.25)

# Calcular salario bruto, descuento (8%) y salario neto
salario_bruto = pago_normal + pago_extra
descuento = salario_bruto * 0.08
salario_neto = salario_bruto - descuento

# Mostrar los resultados finales
print("-" * 40)
print(f"RESUMEN DE PAGO PARA: {nombre}")
print(f"Horas normales trabajadas: {horas_normales} (Pago: ${pago_normal:,.2f})")
print(f"Horas extra trabajadas: {horas_extra} (Pago: ${pago_extra:,.2f})")
print(f"Salario total (bruto): ${salario_bruto:,.2f}")
print(f"Descuento salud y pensión (8%): ${descuento:,.2f}")
print(f"Salario neto a pagar: ${salario_neto:,.2f}")
print("-" * 40)
