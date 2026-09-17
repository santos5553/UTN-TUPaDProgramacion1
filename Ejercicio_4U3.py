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