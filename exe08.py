# Exercicio 8

produtos = []

for _ in range(3):
    produto = float(input(f'Informe o valor do {_ + 1}º produto R$: '))
    produtos.append(produto)

menor = produtos[0]
if produtos[1] < produtos[0] and produtos[1] < produtos[2]:
    menor = produtos[1]
    print(f"Voce deve comprar o produto 2")
elif produtos[2] < produtos[0] and produtos[2] < produtos[1]:
    menor = produtos[2]
    print(f"Voce deve comprar o produto 3")
else:
    print(f"Voce deve comprar o produto 1")

