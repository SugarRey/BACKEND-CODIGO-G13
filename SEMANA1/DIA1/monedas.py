#Programa para convertir monedas
#version 1.0
#Input - entradas

montoOrigen = input("Ingrese el moto en soles: ")

#proceso
print("Opcion 1 = soles a dolares")
print("opcion 2 = dolares a soles")
opcion = input("Elija una opcion: ")
if(opcion =="1"):
   montoDolares = float(montoOrigen) / 3.8
   montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
   #output - salidas
   print("el monto e n dolares es: " + str(montoDolaresFormato))
elif(opcion =="2"):
   montoSoles = float(montoOrigen) * 3.8
   montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
   #output - salidas
   print("el monto en soles es: ", montoSolesFormato)
else:
   print("ALERTA, debe seleccionar una opcion")



