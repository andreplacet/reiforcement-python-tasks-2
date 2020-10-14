# Exercicio 20

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota3 + nota1 + nota2) / 3

if media >= 7 and media != 10:
    print(f"Aprovado com media {media}")
elif media < 7 :
    print(f"Reprovado com media {media}")
else:
    print(f"Aprovado com Distinção, média {media}")
