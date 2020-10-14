# Exercicio 14

n1 = float(input('Digite o valor da primeira media: '))
n2 = float(input('Digite o valor da segunda media: '))

media = (n1 + n2) / 2

if 9 <= media <= 10:
    print(f' media da primeira prova: {n1}')
    print(f'A media da segunda prova: {n2}')
    print('Você tirou um A!')
    print(f'Sua media é de: {media}')
    print(f'você foi aprovado!!')

elif 7.5 <= media < 9:
    print(f' media da primeira prova: {n1}')
    print(f'A media da segunda prova: {n2}')
    print('Você tirou um B!')
    print(f'Sua media é de: {media}')
    print(f'você foi aprovado!!')

elif 6.5 <= media < 7.5:
    print(f' media da primeira prova: {n1}')
    print(f'A media da segunda prova: {n2}')
    print('Você tirou um C!')
    print(f'Sua media é de: {media}')
    print(f'você foi aprovado!!')

elif 4 <= media < 6:
    print(f' media da primeira prova: {n1}')
    print(f'A media da segunda prova: {n2}')
    print('Você tirou um D!')
    print(f'Sua media é de: {media}')
    print(f'você foi reprovado!!')

elif media < 4:
    print(f' media da primeira prova: {n1}')
    print(f'A media da segunda prova: {n2}')
    print('Você tirou um E!')
    print(f'Sua media é de: {media}')
    print(f'você foi reprovado!!')
