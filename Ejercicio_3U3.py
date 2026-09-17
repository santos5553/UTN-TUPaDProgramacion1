#Ejercicio 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = ""
while operador.isalpha() == False:
    operador = input("Ingrese el nombre del operador: ")
    if operador.isalpha() == False:
        print("El nombre del operador debe contener solo letras.")

opcion = ""
while opcion != "5":
    print("\n1" + "="*35)
    print(f"Sistema de turnos - Operador: {operador}")
    print("="*35)
    print("1) Reservar turno")
    print("2) Cancelar turno (por nombre del paciente)")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Seleccione una opcion: ")
    if opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 5:
        print("Opcion invalida. Intente nuevamente.")
    elif opcion == "1":
        dia = ""
        while dia.isdigit() == False or (dia != "1" and dia != "2"):
            dia = input("Elija el dia para reservar turno (1= Lunes, 2= Martes): ")
            if dia.isdigit() == False or (dia != "1" and dia != "2"):
                print("Opcion invalida. Ingrese 1 o 2.")

        paciente = ""
        while paciente.isalpha() == False:
            paciente = input("Inngrese el nombre del paciente: ")
            if paciente.isalpha() == False:
                print("El nombre del paciente debe contener solo letras")

        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print(f"El paciente {paciente} ya tiene un turno reservado para el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado para {paciente} el lunes.")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado para {paciente} el lunes.")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado para {paciente} el lunes.")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado para {paciente} el lunes.")
            else:
                print("No hay turnos disponibles para el lunes.")

        elif dia == "2":
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print(f"El paciente {paciente} ya tiene un turno reservado para el martes.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno reservado para {paciente} el martes.")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno reservado para {paciente} el martes.")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno reservado para {paciente} el martes.")
            else:
                print("No hay turnos disponibles para el martes.")

    elif opcion == "2":
        dia = ""
        while dia.isdigit() == False or (dia != "1" and dia != "2"):
            dia = input("Elija el dia para cancelar turno (1= Lunes, 2= Martes): ")
            if dia.isdigit() == False or (dia != "1" and dia != "2"):
                print("Opcion invalida. Ingrese 1 o 2.")

        paciente = ""
        while paciente.isalpha() == False:
            paciente = input("Ingrese el nombre del paciente para cancelar turno: ")
            if paciente.isalpha() == False:
                print("El nombre del paciente debe contener solo letras")

        if dia == "1":
            if paciente == lunes1:
                lunes1 = ""
                print(f"Turno 1 cancelado para {paciente} el lunes.")
            elif paciente == lunes2:
                lunes2 = ""
                print(f"Turno 2 cancelado para {paciente} el lunes.")
            elif paciente == lunes3:
                lunes3 = ""
                print(f"Turno 3 cancelado para {paciente} el lunes.")
            elif paciente == lunes4:
                lunes4 = ""
                print(f"Turno 4 cancelado para {paciente} el lunes.")
            else:
                print(f"No se encontró un turno reservado para {paciente} el lunes.")

        elif dia == "2":
            if paciente == martes1:
                martes1 = ""
                print(f"Turno 1 cancelado para {paciente} el martes.")
            elif paciente == martes2:
                martes2 = ""
                print(f"Turno 2 cancelado para {paciente} el martes.")
            elif paciente == martes3:
                martes3 = ""
                print(f"Turno 3 cancelado para {paciente} el martes.")
            else:
                print(f"No se encontró un turno reservado para {paciente} el martes.")

    elif opcion == "3":
        dia = ""
        while dia.isdigit() == False or (dia != "1" and dia != "2"):
            dia = input("Elija el dia para ver agenda (1= Lunes, 2= Martes): ")
            if dia.isdigit() == False or (dia != "1" and dia != "2"):
                print("Opcion invalida. Ingrese 1 o 2.")

        if dia == "1":
            print("\n----Agenda del lunes----")
            print(f"Turno 1: {lunes1 if lunes1 != " " else "Libre"}")
            print(f"Turno 2: {lunes2 if lunes2 != " " else "Libre"}")
            print(f"Turno 3: {lunes3 if lunes3 != " " else "Libre"}")
            print(f"Turno 4: {lunes4 if lunes4 != " " else "Libre"}")
        elif dia == "2":
            print("\n----Agenda del martes----")
            print(f"Turno 1: {martes1 if martes1 != " " else "Libre"}")
            print(f"Turno 2: {martes2 if martes2 != " " else "Libre"}")
            print(f"Turno 3: {martes3 if martes3 != " " else "Libre"}")

    elif opcion == "4":
        lunes_ocupados = 0
        if lunes1 != "": lunes_ocupados += 1
        if lunes2 != "": lunes_ocupados += 1
        if lunes3 != "": lunes_ocupados += 1
        if lunes4 != "": lunes_ocupados += 1
        lunes_disponibles = 4 - lunes_ocupados

        martes_ocupados = 0
        if martes1 != "": martes_ocupados += 1
        if martes2 != "": martes_ocupados += 1
        if martes3 != "": martes_ocupados += 1
        martes_disponibles = 3 - martes_ocupados

        print("\n----Resumen general----")
        print(f"Turnos ocupados el lunes: {lunes_ocupados} | Turnos disponibles: {lunes_disponibles}")
        print(f"Turnos ocupados el martes: {martes_ocupados} | Turnos disponibles: {martes_disponibles}")

        if lunes_ocupados > martes_ocupados:
            print("El lunes tiene mas turnos ocupados.")
        elif martes_ocupados > lunes_ocupados:
            print("El martes tiene mas turnos ocupados.")
        else:
            print("Los dos dias tienen la misma cantidad de turnos ocupados.")

    elif opcion == "5":
        print(f"\nSaliendo del sistema. Adios, {operador}.")