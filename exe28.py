# Exercicio 28

file = 0
picanha = 0
alcatra = 0

pedido = str(input('Escolha o tipo de carne\n'
                   '[F]ilé - [A]lcatra - [P]icanha\n'
                   '--> ')).upper()

if pedido[0] == 'F':
    quantidade = float(input('Quantos kilos de filé? '))
    if quantidade > 5.0:
        file = 4.90
    else:
        file = 5.80

    total_compra = quantidade * file
    pagamento = str(input(f'O valor total da compra é de R${total_compra:.2f}\n'
                          f'gostaria de pagar com cartão Tabajara? [s]im/[n]ão\n'
                          f'--> ')).upper()
    if pagamento[0] == 'S':
        desconto = total_compra * 0.05
        print(f'Produto: Filé\n'
              f'Quantidade KG: {quantidade:.3f} - preço KG {file:.2f}\n'
              f'Valor Total: R${total_compra:.2f}\n'
              f'Tipo de Pagamento: Cartão Tabajara\n'
              f'Desconto: R${desconto:.2f}\n'
              f'Total: R${total_compra - desconto:.2f}')
    else:
        print(f'Produto: Filé\n'
              f'Quantidade KG: {quantidade:.3f} - preço KG {file:.2f}\n'
              f'Tipo de Pagamento: Dinheiro\n'
              f'Total: R${total_compra:.2f}')

if pedido[0] == 'A':
    quantidade = float(input('Quantos kilos de alcatra? '))
    if quantidade > 5.0:
        alcatra = 5.90
    else:
        alcatra = 6.80

    total_compra = quantidade * alcatra
    pagamento = str(input(f'O valor total da compra é de R${total_compra:.2f}\n'
                          f'gostaria de pagar com cartão Tabajara? [s]im/[n]ão\n'
                          f'--> ')).upper()
    if pagamento[0] == 'S':
        desconto = total_compra * 0.05
        print(f'Produto: Filé\n'
              f'Quantidade KG: {quantidade:.3f} - preço KG {alcatra:.2f}\n'
              f'Valor Total: R${total_compra:.2f}\n'
              f'Tipo de Pagamento: Cartão Tabajara\n'
              f'Desconto: R${desconto:.2f}\n'
              f'Total: R${total_compra - desconto:.2f}')
    else:
        print(f'Produto: Alcatra\n'
              f'Quantidade KG: {quantidade:.3f} - preço KG {alcatra:.2f}\n'
              f'Tipo de Pagamento: Dinheiro\n'
              f'Total: R${total_compra:.2f}')

if pedido[0] == 'P':
    quantidade = float(input('Quantos kilos de picanha? '))
    if quantidade > 5.0:
        picanha = 6.90
    else:
        picanha = 7.80

    total_compra = quantidade * picanha
    pagamento = str(input(f'O valor total da compra é de R${total_compra:.2f}\n'
                          f'gostaria de pagar com cartão Tabajara? [s]im/[n]ão\n'
                          f'--> ')).upper()
    if pagamento[0] == 'S':
        desconto = total_compra * 0.05
        print(f'Produto: Picanha\n'
              f'Quantidade KG: {quantidade:.3f} - preço KG {picanha:.2f}\n'
              f'Valor Total: R${total_compra:.2f}\n'
              f'Tipo de Pagamento: Cartão Tabajara\n'
              f'Desconto: R${desconto:.2f}\n'
              f'Total: R${total_compra - desconto:.2f}')
    else:
        print(f'Produto: Filé\n'
              f'Quantidade KG: {quantidade:.3f} - preço KG {picanha:.2f}\n'
              f'Tipo de Pagamento: Dinheiro\n'
              f'Total: R${total_compra:.2f}')

print('Obrigado, Volte Sempre!')