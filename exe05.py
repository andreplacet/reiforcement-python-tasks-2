# Exercicio 5

notas = []

for _ in range(2):
    nota = float(input(f'Informe a {_ + 1}º nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

if 7 <= media < 10:
    print(f'Sua média foi de {media:.1f}, e você foi aprovado!')
elif media == 10:
    print(f'Sua média foi de {media:.0f}, e voce foi aprovado com méritos! Parabéns!')
else:
    print(f'Sua média foi de {media:.1f}, e você foi reprovado!')
