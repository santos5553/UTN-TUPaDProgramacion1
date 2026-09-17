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