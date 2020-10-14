# Exercicio 10

horario = str(input('Qual periodo voce estuda?\n[V] - Vespertino\n[O] - Diurno\n[N] - Nohorario\n --> ')).upper()

if horario == 'V':
    print("Boa Tarde")
elif horario == 'D':
    print("Bom dia")
elif horario == 'N':
    print("Boav Noite")
else:
    print("Entrada invalida")