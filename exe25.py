# Exercicio 25

perguntas = ['Telefonou para a vitima?', 'Esteve no local do crime?', 'Mora perto da vitima?',
             'Devia algo para a vítima?', 'Ja trabalhou com a vitima?']

respostas = []

print('Voce é suspeito de assasinato!\nResponda cada com pergunta com 1 para SIM e 0 para NÃO')

for pergunta in perguntas:
    resposta = int(input(f'{pergunta} '))
    if resposta == 1:
        respostas.append(resposta)
    else:
        pass

veredito = ''

if len(respostas) == 0:
    veredito = 'Inocente'
else:
    if len(respostas) == 5:
        veredito = 'Assasino'
    elif len(respostas) == 2:
        veredito = 'Suspeito'
    elif len(respostas) >= 3 or len(respostas) <= 4:
        veredito = 'Cumplice'

print(f'De acordo com as respostas, seu veredito foi {veredito}')
