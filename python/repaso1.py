print("===TIENDA EL DESCANSO===")
print("porfavor ingrese la siguiente informacion: \n")

cliente =input("nombre cliente: ")
producto =input("nombre producto: ")
cantidad =int(input("cantidad: "))
precio = float(input("precio: "))

#variable para preguntar si la compra es a domicilio
domiciolio =input("la compra es para domicilio (SI - NO): ")
#condicional verificar que respondio el usuario

#upper() convierte en mayuscula .lower)minuscula
if domiciolio.upper() =="NO":
   print("===RESUMEN COMPRA===")
   print(f"""
   -cliente:{cliente}
   -producto:{producto}
   -cantidad:{cantidad}
   -precio:{precio}
   -total:{cantidad*precio}
   
gracias por su compra.
   """)
elif domiciolio.upper() =="SI":
   direccion=input("ingrese municipio del envio(MEDELLIN, ENVIGADO, BELLO):") 
   valor_domicio=0
   if direccion.lower()=="medellin":
      valor_domicio= 5000 
   elif direccion.lower()=="envigado":
      valor_domicio=10000
   elif direccion.lower()=="bello":
      valor_domicio=8000

   else:
      print("direccion invalida")

   print("===RESUMEN COMPRA===")
   print(f"""
       -cliente:{cliente}
       -producto:{producto}
       -cantidad:{cantidad}
       -precio:{precio}
       -subtotal:{cantidad*precio}
       -domicio:{valor_domicio}
       -total pagar{valor_domicio + (cantidad*precio)}

    gracias por su compra.    """)
else:
      print("direccion invalida")