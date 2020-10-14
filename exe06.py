# Exercicio 6

numeros = []

for _ in range(3):
    num = int(input(f'Informe o {_ + 1} número: '))
    numeros.append(num)

print(f'O maior número digitado foi {max(numeros)}')
