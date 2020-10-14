# Exercicio 19

numero = int(input("Entre com um numero inteiro e menor que 1000: "))

if numero > 1000:
    print("Numero invalido")
else:
    unidade = numero % 10
    dezena = int(((numero - unidade) / 10) % 10)
    centena = int((numero - dezena) / 10)
    print(f"{centena} centena(s) , {dezena} dezena(s) e {unidade} unidade(s)")
