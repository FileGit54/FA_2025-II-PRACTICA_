sumap = sumai = 0
while True:
    num = int(input("Ingrese un número (0 salir): "))
    
    if num<0:
        print("Número inválido. Ingrese nuevamente: ")
        continue

    if num ==0:
        break
    if num%2 ==0:
        sumap+=num
    else:
        sumai += num

print("\nSuma de pares: ", sumap)
print("suma de imapres: ", sumai)