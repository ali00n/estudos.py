nummero = int(input("digite um numero positivo maior que um "))
if numero > 1:
    for i in range(2, numero):
        if (numero  % i) == 0:
            print(f"{numero} nao é um numero primo")
            break
    else:
        print("por favor, insira um numero positivo ")
else:
    print("por favor, insira um numero positivo maior do que 1 ")
