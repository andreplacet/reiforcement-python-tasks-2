#Exercicio 3

sexo = str(input('Informe seu sexo: [M]asculino / [F]eminino: ')).upper()

if sexo[0] == 'M':
    print('Sexo masculino!')
elif sexo[0] == 'F':
    print('Sexo Feminino!')
else:
    print('Sexo Invalido! ')
