# Exercicio 1

lista = []

for _ in range(2):
    num = int(input(f'{_ + 1}º número: '))
    lista.append(num)

print(f'O maior número digitado foi {max(lista)}')


'''
Lógica pura, sem uso de funções built-in

num1 = int(input('Informe o primeiro número: '))
num1 = int(input('Informe o segundo número: '))

if num1 > num2:
    maior = num1
    print(f'O maior número digitado foi: {maior}')
elif num1 == num2:
    print(f'Os números são iguais')
else:
    maior = num2
    print(f'O maior número digitado foi: {maior}')
'''

