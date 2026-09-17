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