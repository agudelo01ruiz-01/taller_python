
# Ejercicio 1: try / except básico
"""  
# Sin manejo de errores, ingresar "hola" en lugar de un número
# provocaría un ValueError y el programa se detendría.

try:
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: debe ingresar un número entero válido.")

"""    
# Ejercicio 2: División segura con ZeroDivisionError

""" 
try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor   = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese únicamente valores numéricos.")
""" 
# Ejercicio 3: else y finally

""" 
# else  → se ejecuta solo si NO ocurrió ninguna excepción
# finally → se ejecuta SIEMPRE, con o sin error

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un número entero.")
else:
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")

""" 
# Ejercicio 4: Solicitar un dato válido hasta que el usuario lo ingrese correctamente

""" 
while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        break   # sale del ciclo si el valor es válido
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")

""" 
# Ejercicio 5: raise — lanzar una excepción personalizada

""" 
def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n      = int(input("¿Cuántas notas va a ingresar? "))
    notas  = []
    for i in range(n):
        nota = float(input(f"  Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")

"""
#---ejemplos---
 
"""
while True:
    try:
        nota=float(input("ingrese nota: "))
    except ValueError:
        print("ingresa una nota valida. ") 

while True:
    try:
            cantidad_notas=int(input("cuantas notas quieres registrar: "))
            lista_notas=[]

            for i in range(cantidad_notas):
                nota=float(input("ingrese una nota: "))
                lista_notas.append(nota)
    except ValueError:
        print("notas registradas: ", lista_notas)
        promedio=sum(lista_notas)/len(lista_notas)
        print(f"promedio: {promedio}")

        if promedio<=2:
             print("basico")
        
        if promedio<=4:

             print("aceptable")
        
        if promedio<=5:
             
            print("bien")
        

    except ValueError:
        print("ingresa una cantidad valida")

"""

#1.Solicitar al usuario dos números y un operador (+, -, *, /).
#Manejar con try/except la división entre cero y la entrada no numérica.

"""
try:
    # Solicitar los dos números y el operador
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operador = input("Ingresa un operador (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2  # Esto lanzará ZeroDivisionError si num2 es 0
    else:
        print("Operador no válido.")
        resultado = None

    # Mostrar el resultado si la operación fue exitosa
    if resultado is not None:
        print(f"El resultado es: {resultado}")

except ValueError:
    print("Error: Debes ingresar un valor numérico válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
"""

#2.Pedir el nombre de un archivo al usuario e intentar abrirlo con open(). 
#Capturar FileNotFoundError y mostrar un mensaje claro.

"""
nombre_archivo = input("Introduce el nombre del archivo: ")

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print("Archivo abierto con éxito.")
        print(contenido)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo}'. Comprueba que el nombre y la ruta sean correctos.")
"""


#3.Solicitar una fecha en formato DD/MM/AAAA. 
#Usar try/except para capturar ValueError si el formato o los valores son inválidos.

"""

from datetime import date

try:
    fecha_str = input("Ingrese una fecha en formato DD/MM/AAAA: ")
    partes = fecha_str.split("/")
    
    if len(partes) != 3:
        raise ValueError
        
    dia = int(partes[0])
    mes = int(partes[1])
    anio = int(partes[2])
    fecha_valida = date(anio, mes, dia)
    
    print(f"Fecha ingresada correctamente: {fecha_str}")
    
except ValueError:
    print("Error: El formato o los valores de la fecha son inválidos.")
"""

#4.Crear una función raiz_cuadrada(n)
#que lance ValueError si n es negativo. Llamarla dentro de un try/except e informar al usuario.

"""
def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("Error: El número es negativo")
    return n ** 0.5

try:
    resultado = raiz_cuadrada(-9)
    
except ValueError as error:
    print(error)
"""


#5.Solicitar números al usuario en un ciclo hasta que ingrese 'fin'.
#Acumular los válidos con try/except e ignorar los inválidos, 
#mostrando al final la cantidad de valores aceptados y su promedio.

suma = 0
cantidad = 0

while True:
    entrada = input("Ingrese un número o 'fin': ")
    
    if entrada == "fin":
        break
        
    try:
        numero = float(entrada)
        suma = suma + numero
        cantidad = cantidad + 1
    except:
        print("Error: Eso no es un número válido. Inténtelo de nuevo.")

if cantidad > 0:
    promedio = suma / cantidad
    print("Cantidad de valores aceptados:", cantidad)
    print("Promedio:", promedio)
else:
    print("No se ingresaron números válidos.")

