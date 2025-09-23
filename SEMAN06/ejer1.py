num = int(input("Ingrese un número positivo: "))
print()

while num<=0:
    num = int(input("Erro.Ingrese un número positivo: "))

i = 1
while i <=12:
    print(f"{i} x {num} = {i*num}")
    i+=1
