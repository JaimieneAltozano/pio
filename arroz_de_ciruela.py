pio = True
espacios = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
placas = []

while pio:
    print("\nMenu: \n1. Mostrar espacios\n2. Ingresar carro\n3. Sacar carro\n4. Salir")
    options = int(input("Option: "))
    if options == 4:
        print("Búsquese otro parqueadero")
        pio = False
    elif options == 1:
        print(espacios)
    elif options == 2:
        spaceNumber = int(input("Número de espacio a ocupar: "))
        placa = input("Placa: ")
        if not(placa in espacios):
            placas.append(placa)
            espacios[spaceNumber - 1] = placa
        else:
            print("El carro ya está aquí")
    elif options == 3:
        placa = input("Placa: ")
        if placa in espacios:
            number = espacios.index(placa)
            espacios[number] = number + 1
            placas.remove(placa)
            print("sacar carro")
        else:
            print("Te equivocas de parqueadero")


  #if spaceNumber < 1 or spaceNumber > 10:
    #         print("Espacio inválido")
    #    elif isinstance(espacios[spaceNumber-1], int):
    #        espacios[spaceNumber-1] = placa
    #        print("Carro ingresado")
    #    else:
    #        print("Ese espacio ya está ocupado")