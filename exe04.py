# Exercicio 4

leta = str(input('Digite uma letra: ')).lower()
vogais = ('a', 'e', 'i', 'o', 'u')

if leta in vogais:
    print(f'a letra {leta} é uma vogal')
else:
    print(f'A letra {leta} é uma consoante!')
