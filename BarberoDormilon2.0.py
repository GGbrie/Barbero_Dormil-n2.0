def pedircliente():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto=True
        except ValueError:
            print('Ya esta lleno')
    return num
 
salir = False
opcion = 0
 
while not salir:

    print ("1. Cliente entra")
    print ("2. Pasa a atender")
    print ("3. Eatado del barbero")
    print (" ")

    print ("Elige una opcion")
    print ("Opcion 1")
    print ("Opcion 2")
    print ("Opcion 3")
    print ("4. Salir")

 
    opcion = pedircliente()
 
    if opcion == 1:
        print (" ------------------- Barbero se despierta y atiende al cliente ------------------- ")
    elif opcion == 2:
        print (" ------------------- Otro cliente entra para esperar su turno ------------------- ")
    elif opcion == 3:
        print(" ------------------- Cliente se va y el barbero se duerme ------------------- ")
    elif opcion == 4:
        salir = True
 
print ("Fin")
