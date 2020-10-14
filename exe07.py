# Exercicio 7

numeros = []

for _ in range(3):
    num = int(input(f'Informe o {_ + 1} número: '))
    numeros.append(num)

print(f"O maior valor é {max(numeros)}")
print(f"O maior valor é {min(numeros)}")

