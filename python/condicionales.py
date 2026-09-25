"""
#crear variables
print("por favor ingrese los siguientes  dato\n")
var_nombre = input("nombre:") 
var_edad = int(input("edad:"))

#crar condicion

if var_edad >= 18 :
    print(f"{var_nombre} eres mayor de edad")
else:
    print(f"{var_nombre} eres menor de edad")
"""

#crear variables 2
"""
print("ejercicio: Nota final")
var_nombre = input("nombre:")
var_notafinal = float(input("nota final:"))

if var_notafinal < 0 or var_notafinal > 5 :
    print("nota invalida.")

elif: var_notafinal >= 3.5 : 
    print(f"estudiante {var_nombre} gano👍")

else:
    print(f"estudiante {var_nombre} perdio👎")
"""

# Ejercicio 1: Determinar si un número es positivo, negativo o cero

""" 
numero = float(input("Ingrese un número: "))

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print("El número es cero")

"""
#Ejercicio 2: Determinar si un número es par o impar


"""
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:      # si el residuo es 0 → es par
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

# Ejercicio 3: Clasificar una nota académica

"""
"""

# Ejercicio 3: Clasificar una nota académica

nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
else:
    print("Desempeño bajo")
"""

# Ejercicio 4: Determinar el mayor de tres números

"""
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

print(f"El mayor de los tres números es: {mayor}")

"""

#1Elaborar un algoritmo que solicite el nombre y la edad de una persona y determine si es mayor o menor de edad.
#.Se considera mayor de edad a partir de los 18 años.
#.Validar que la edad ingresada no sea un valor negativo; si lo es, mostrar un mensaje de error.
#.Si la persona es menor de edad, calcular y mostrar cuántos años le faltan para cumplir la mayoría de edad.
#.Al finalizar, debe mostrar el nombre, la edad ingresada y el resultado correspondiente.


"""
name = input("nombre: ")
edad = int(input("edad: "))

if edad <= 0 :
    print("reviza")
elif edad >= 18 :
    print(f"hola{nombre}tu edad es{edad}, puedes pasar")
else:
    print(f"hola({nombre}tu edad es{edad}, te falta{18-edad}, para ingresar ")   

"""

"""
#2.Elaborar un algoritmo que solicite el nombre de un estudiante y su calificación final, en una escala de 0.0 a 5.0.
#Se aprueba con una calificación igual o superior a 3.0.
#Debe validar que la calificación esté dentro del rango permitido (0.0 a 5.0); si no lo está, mostrar un mensaje de error y no continuar con la evaluación.
#Además de aprobado/reprobado, clasificar el desempeño: "Excelente" (4.5–5.0), "Bueno" (3.5–4.4), "Aceptable" (3.0–3.4) o "Insuficiente" (menor a 3.0).
#Al finalizar, debe mostrar el nombre del estudiante, la calificación ingresada, el resultado (aprueba o reprueba) y la clasificación del desempeño.

nombre = input("nombre: ")
nota = float(input("nota: "))

#0-3= insuficiente
if nota< 0 or nota > 5 :
    print(f"{nota} insuficiente")

elif nota < 3:
    print(f"{nota}aceptable")

elif nota < 3.5:
    print(f"{nota}aceptable")

elif nota < 4.5:
    print(f"{nota}aceptable")

else :
    print(f"{nota}exelente")

"""

#3.Elaborar un algoritmo que solicite el nombre de un cliente y el valor total de una compra, y calcule el descuento según el valor:


nombre = input("nombre")
total_compra = float(input("total compra:"))

if total_compra < 100000:
    print(f"""
    -cliente:{nombre}
    -compra:{total_compra}no tiene descuento
    """)
elif total_compra < 299999 :
    #descuento 10%

    print(f"""
    -cliente:{nombre}
    -compre:{total_compra}
    -descuento:{total_compra * 0.1}
    -total pagar:{total_compra - (total_compra*0.1)}
""")

elif total_compra < 499999 :
    #descuento 15%

    print(f"""
    -cliente:{nombre}
    -compre:{total_compra}
    -descuento:{total_compra * 0.15}
    -total pagar:{total_compra - (total_compra*0.15)}
""")

else:
    print(f"""
        -cliente:{nombre}
        -compre:{total_compra}
        -descuento:{total_compra * 0.2}
        -total pagar:{total_compra - (total_compra*0.2)}""")



