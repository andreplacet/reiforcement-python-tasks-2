# Exercicio 9

numeros = []

for _ in range(3):
    num = int(input(f"Informe o {_ + 1} número: "))
    numeros.append(num)

lista = sorted(numeros, reverse=True)

print(lista)
