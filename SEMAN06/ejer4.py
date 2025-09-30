g = input("genere una contraseña: ")

print("-------------------------------------")
print("|      Valida tu contraseña        |")
print("|                                  |")
print("| 1. Ud. tiene 3 intentos          |")
print("------------------------------------")

intentos = 3

while(intentos > 0):
    c = input("Ingrese la contreaseña: ")

    if g == c:
        print("\nAcceso concedidio. Bienvenido al sistema.")
        break
    else:
        intentos-=1
        print("Contrasaeñqa incorrecta. Intentos restantes ",intentos)

else: print("Acceso denegado! cerrando sistema.")