#Programa para convertir monedas
#version 1.0
#Input - entradas

montoOrigen = input("Ingrese el tipo de cambio: ")
opcion = ""
while(opcion == ""):
#proceso
   print("============================")
   print("Opcion 1 = Soles a Dolares")
   print("opcion 2 = dolares a soles")
   print("Opcion 3 = Soles a Euros")
   print("OPcion 4 = Euros a Soles")
   print("============================")

   opcion = input("Elija una opcion: ")
   if(opcion =="1"):
      montoDolares = float(montoOrigen) / 3.8
      montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
      #output - salidas
      print("el monto en dolares es: " + str(montoDolaresFormato))
   elif(opcion =="2"):
      montoSoles = float(montoOrigen) * 3.8
      montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
      #output - salidas
      print("el monto en soles es: ", montoSolesFormato)
   elif(opcion == "3"):
      montoEuros = float(montoOrigen) / 4.07
      montoEurosFormato = "$/. {:,.2f}".format(montoEuros)
      #la salida si es true la condicion
      print("El monto en Euros es: ", montoEurosFormato)
   elif(opcion == "4"):
      montoSoles = float(montoOrigen) * 4.07
      montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
      #se ejecuta la salida si es true la condicion
      print("El monto en Soles es: ", montoSolesFormato)
   else:
      print("ALERTA, debe seleccionar una opcion")
      salir = input("Desea salir (SI/NO)")
      if(salir == "no"):
         opcion = ""




