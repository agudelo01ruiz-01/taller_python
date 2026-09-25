"""
lista_producto=[] #lista en blancos
cantidad=int(input("cantidad a comprar: "))

for i in range(cantidad):
    producto=input(f"nombre del producto {i+1}: ")
    lista_producto.append(producto)
print(f"productos comprados: {lista_producto}")
""" 
listado_perros=[]
listado_gatos=[]

while True:
    pregunta=int(input("""
1. registrar perro
2. registrar gato
3. listado perros
4. listado gatos
5. salir    
 """))
 

    if pregunta ==1:
        perro= input("ingresar nombre del perro: ")
        listado_perros.append(perro)
        print("perro registrado")
    elif pregunta ==2:
        gato= input("ingresar nombre del gat: ") 
        listado_gatos.append(gato)
        print("gato registrado") 
    elif pregunta ==3:
        print(listado_perros)
    elif pregunta ==4:
        print(listado_gatos)
    else:
        print("opcion invalida")

