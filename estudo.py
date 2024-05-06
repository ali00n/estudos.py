inicio = int(input("digite um numero inicial "))
fim = int(input("digite o numero final "))

print(f"numeros pares entre {inicio} e {fim}")
for numero in range(inicio, fim + 2):
    if numero % 2 ==0:
        print(numero)
