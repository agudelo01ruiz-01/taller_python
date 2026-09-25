#4.Elaborar un algoritmo que solicite el nombre de una ciudad y la temperatura actual en grados Celsius, y la clasifique según estos rangos:
#Menor a 10 °C → "Muy fría".
#De 10 °C a 17 °C → "Fría".
#De 18 °C a 25 °C → "Templada".
#De 26 °C a 32 °C → "Caliente".
#Mayor a 32 °C → "Muy caliente".
#Adicionalmente, indicar si se recomienda llevar abrigo (temperaturas menores a 18 °C).
#Al finalizar, debe mostrar la ciudad, la temperatura registrada, su clasificación y la recomendación.

nombre_ciudad = input("ciudad: ")
temperatura_ciudad = float(input("temperatura: "))

if temperatura_ciudad <= 10 :
    print (f"la ciudad de {nombre_ciudad}{temperatura_ciudad} Muy fría")

elif temperatura_ciudad in range (10, 17) :
    print(f"la ciudad de {nombre_ciudad} {temperatura_ciudad} frio")
elif temperatura_ciudad in range (18, 25) :
    print(f"la ciudad de {nombre_ciudad} {temperatura_ciudad} templado")
elif temperatura_ciudad in range (26, 32) :
    print(f"la ciudad de {nombre_ciudad} {temperatura_ciudad} caliente")

else:
    temperatura_ciudad= "Muy caliente"

# Salida de resultados
print("\2--- RESULTADOS ---")
print(f"Ciudad: {nombre_ciudad}")
print(f"Temperatura registrada: {temperatura_ciudad} °C")

