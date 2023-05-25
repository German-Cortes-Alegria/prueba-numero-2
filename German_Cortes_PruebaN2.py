

opcion=""
carillas=250000
implantes=475000
ortodoncia=800000


while True:
 while opcion!=5:
   print("-----Clinica Dental-----")
   print("-----Diente de Oro-----")
   print("Tratamientos-----------")
   print("1.-Carillas Porcelana---$250000")
   print("2.-implantes dentales---$475000")
   print("3.-Ortodoncia Brackets---$800000")
   print("4.-borrar cotizacion")
   print("5.-Salir")
   print("todos los tratamiento incluyen")
   print("**Limpieza y destartraje**")
   print("**Aplicacin de sellante**")
   print("**Aplicacion de fluor**")
 try:
     opcion=int(input("ingrese una opcion:  "))
     if 6<opcion<0:
        print("opcion fuera de rango")
        
     else:
      opcion=0
 except:
    print("error intente nuevamente")

 if(opcion==1):
        totalT=+carillas
        print("Seleciono tratamieno de Carillas")
 elif opcion==2:
        totalT=+implantes
        print("selecciionotratamiento de implantes")
 elif opcion==3:
        totalT=+ortodoncia
        print("selecciono tratamiento de orodoncia")
 elif opcion==4:
     totalT=0
     print("seleciciono borrar cotizacion")
 elif opcion==5:
    opcion=5
    print("seleciciono salir")
          
 else :
         print("ingrese una opcion valida") 
         while True:
            print("Seleccione que trabajador es")
            print("a.trabajador auxiliar 15%/ desc")
            print("b.trabajador administrativo 10%/ desc")
            print("c.trabajador docente 5%/ desc")
            try:
               descuento=int("ingrese una opcion").lower()
               if descuento!="a" and descuento!="b" and descuento!="c":
                raise Exception()
               else:
                break
            except:
                print("error intenta nuevamente")
         if descuento=="a":
            totalT=totalT*0.85
         elif descuento=="b":
            totalT=totalT*0.9
         elif descuento=="c":
            totalT=totalT*0.95
         else:
            print(f"el total despues de descuento es $ {totalT:.1f}")
            cuotaMensual=totalT/12
            print(f"la cuota mensual seria de ${cuotaMensual:.1f}")
            totalT=0
            cuotaMensual=0




