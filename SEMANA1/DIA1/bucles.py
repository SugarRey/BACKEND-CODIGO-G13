opcion = "0"
while(opcion == "0"):
   print("**********************")
   print("*      OPCIONES      *")
   print("**********************")
   print("1) Opcion 01")
   print("2) Opcion 03")
   print("3) Opcion 04")
   print("4) Salir")
   opcion = int(input("Opcion elegida: "))
   print("Ud. selecion a la opcion" + str(opcion))
   salir = input("desea salir (SI/NO) ")
   if(salir == "no"):
      opcion = "0"

