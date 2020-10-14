# Exercicio 17

print("Calculo para saber se um ano é bissexto ou não")
ano = int(input("Digite um ano a ser verificado: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano %400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")