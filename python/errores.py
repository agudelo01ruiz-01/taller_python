""""
while True:
    try:
        nota=float(input("ingrese nota: "))
    except ValueError:
        print("ingresa una nota valida. ") 
"""
"""
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
