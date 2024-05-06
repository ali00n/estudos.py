numero = int(input("Digite um número positivo maior que 1: "))

if numero <= 1:
    print("Por favor, insira um número positivo maior do que 1.")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
