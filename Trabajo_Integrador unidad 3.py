#Ejercicio 1

cliente= ""
while not cliente.isalpha():
    cliente= input("Ingrese el nombre del cliente: ")
productos= ""
while not productos.isdigit() or int(productos) <= 0:
    productos= input("Ingrese la cantidad de productos: ")
productos= int(productos)

con_descuento= 0
sin_descuento= 0

for i in range(productos):
    print(f"Producto {i+1}:")
    precio= ""
    while not precio.isdigit():
        precio= input("Ingrese el precio del producto: ")
    precio= int(precio)

    descuento= ""
    while descuento.lower() not in ["s", "n"]:
        descuento= input("¿El producto tiene descuento? (s/n): ")

    sin_descuento += precio
    if descuento.lower() == "s":
        con_descuento += precio * 0.9
    else:
        con_descuento += precio

print(f"Cliente: {cliente}")
print(f"Cantidad de productos: {productos}")
print(f"Total sin descuento: ${sin_descuento:.2f}")
print(f"Total con descuento: ${con_descuento:.2f}")
print(f"Ahorro total: ${sin_descuento - con_descuento:.2f}")
print(f"Promedio por producto: ${con_descuento / productos:.2f}")

#Ejercicio 2

intentos= 0
ingreso= False
clave_actual= "python123"

while intentos < 3 and not ingreso:
    intentos +=1
    print(f"Intento {intentos}/3")
    usuario= input("Ingrese su usuario: ")
    clave= input("Ingrese su clave: ")
    if usuario == "alumno" and clave == clave_actual:
        print("Acceso concedido")
        ingreso= True
    else:
        print("Error en usuario o clave")

if not ingreso:
    print("Se han agotado los intentos. Cuenta bloqueada.")
else:
    opcion= ""
    while opcion != "4":
        print("\n1)Estado 2)Cambiar clave 3)Mensaje 4)Salir")
        opcion= input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Opción inválida. Intente nuevamente.")
        else:
            if opcion == "1":
                print("Inscriprito")
            elif opcion == "2":
                nueva_clave= input("Ingrese la nueva clave: ")
                if len(nueva_clave) < 6:
                    print("La clave debe tener al menos 6 caracteres.")
                else:
                    if nueva_clave == input("Confirme la clave nueva: "):
                        clave_actual= nueva_clave
                        print("Clave cambiada exitosamente.")
                    else:
                        print("Las claves no coinciden.")
            elif opcion == "3":
                print("¡Sigue programando!")

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

#Ejercicio 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzada = 0
bloqueado = False

agente = ""
while not agente.isalpha():
    agente = input("Ingrese el nombre del agente: ")
    if agente.isalpha() == False:
        print("El nombre del agente debe contener solo letras.")
print(f"Bienvenido agente {agente}. Comienza la mision!")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    if alarma == True and tiempo <=3:
        bloqueado == True
        print("Sistema bloqueado por alarma.")
        break

    print("\n" + "="*45)
    print(f"ESTADO: Energia: {energia} | Tiempo restante: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma {'ON' if alarma else 'OFF'}")
    print("="*45)
    print("1)Forzar cerradura (-20 energia, -2 tiempo)")
    print("2)Hackear panel (-10 energia, -3 tiempo)")
    print("3)Descansar 8+15 energia, -1 tiempo)")

    accion = ""
    while accion.isdigit() == False or int(accion) < 1 or int(accion) >3:
        accion = input("Seleccione una accion (1-3): ")
        if accion.isdigit() == False or int(accion) < 1 or int(accion) >3:
            print("Error debe ingresar un numero entre 1 y 3.")

    if accion == "1":
        energia -= 20
        tiempo -= 2
        racha_forzada += 1

        if racha_forzada == 3:
            alarma = True
            print("¡CERRADURA TRABADA! Intentas 3 veces seguidas y se activo la alarma")
        else:
            if energia < 40 and not alarma:
                print("¡ALERTA! Energia baja (<40). Hay riesgo de activar la alarma.")
                peligro = ""
                while peligro.isdigit() == False or int(peligro) < 1 or int(peligro) > 3:
                    peligro = input("Ingrese un numero de riesgo (1-3): ")
                    if peligro.isdigit() == False or int(peligro) < 1 or int(peligro) > 3:
                        print("Error ingrese un numero valido (1 - 3): ")

                if peligro == "3":
                    alarma = True
                    print("¡ERROR! Elegiste la opcion incorrecta y se activo la alarma.")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡BIEN! Lograste forzar y abrir 1 cerradura.")

    elif accion == "2":
        racha_forzada = 0 
        energia -= 10
        tiempo -= 3 
        print ("Hackeando el sistema...")
        for i in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {i}/4 - El Codigo actual es :{codigo_parcial}")

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                codigo_parcial = ""
                print("¡Codigo completado! Se abrio 1 cerradura.")

    elif accion == "3":
        racha_forzada = 0 
        tiempo -= 1 
        energia = min(100, energia + 15)
        print(f"Descansas un momento. Tu energia se restablece a {energia}.")


print("\n" + "="*45)
if cerraduras_abiertas == 3:
    print(f"¡GANASTE! Felicidades agente {agente} abriste las 3 cerraduras y superaste la boveda.")
elif bloqueado:
    print("¡PERDISTE! La alarma se activo y el sistema se cerro permanentemente.")
else:
    print(f"¡PERDISTE! Agente {agente} te quedaste sin recursos (Eneriga: {energia}, Tiempo: {tiempo}).")
print("="*45)

#Ejercicio 5

print("--- BIENVENIDO A LA ARENA ---")

gladiador = ""
while gladiador.isalpha() == False:
    gladiador = input("Ingresa tu nombre Gladiador: ")
    if gladiador.isalpha() == False:
        print("Tu nombre solo puede llevar letras.")


vida_g = 100
vida_e = 100
pociones = 3 
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_g > 0 and vida_e > 0:
    if turno_gladiador == True:
        print(f"\n{gladiador} (HP: {vida_g}) vs Enemigo (HP: {vida_e}) |Pociones: {pociones} ")
        print("Elige una accion: \n1. Ataque pesado\n2. Rafaga veloz\n3. Curar")

        opcion = ""
        while opcion.isdigit() == False or (opcion != "1" and opcion != "2" and opcion != "3"):
            opcion = input( "Elige una accion: ")
            if opcion.isdigit() == False or (opcion != "1" and opcion != "2" and opcion != "3"):
                print("Error ingresaste un numero no valido.")

        if opcion == "1":
            daño_final = float(ataque_pesado)
            if vida_e < 20:
                daño_final = ataque_pesado * 1.5
            vida_e -= int(daño_final)
            print(f"Atacaste al enmeigo por {daño_final} puntos de daño.")

        elif opcion == "2":
            print("Inicias una rafaga de golpes")
            for a in range (3):
                vida_e -= 5
                print("Golpe connectado por 5 de daño.")

        elif opcion =="3":
            if pociones > 0:
                vida_g += 30
                pociones -= 1
            else:
                print("No te quedan pociones")

        if vida_e > 0:
            turno_gladiador = False

    else:
        vida_g -= ataque_enemigo
        print(f"El enemigo te ataca por {ataque_enemigo} puntos de daño.")

        turno_gladiador = True

print("\n" + "="*35)
if vida_g > 0:
    print(f" ¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("¡DERROTA! Perdiste la batalla.")