# Exercicio 27

morangos = float(input('Quantos quilos de morango? '))
macas = float(input('Quanto quilos de maçã? '))

preco_morango = 0
preco_maca = 0
desconto = 0

if morangos > 5.0:
    preco_morango = 2.20
else:
    preco_morango = 2.50

if macas > 5.0:
    preco_maca = 1.50
else:
    preco_maca = 1.80

peso_total = morangos + macas
total = (morangos * preco_morango) + (macas * preco_maca)
total_sem_desconto = (morangos * preco_morango) + (macas * preco_maca)

if total > 25 or peso_total > 8:
    desconto = total * 0.10
    total -= desconto

print(f'Voce comprou {morangos}Kg de Morango - R${preco_morango:.2f}Kg\n'
      f'total - R${morangos * preco_morango:.2f}\n'
      f'Voce comprou {macas}Kg de Maçã - R${preco_maca:.2f}Kg\n'
      f'total - R${morangos * preco_maca:.2f}\n'
      f'Total bruto - R${total_sem_desconto}\n'
      f'Desconto - R${desconto:.2f}\n'
      f'Total a pagar: R${total:.2f}')
