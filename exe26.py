# Exercicio 26

print(f'O preço atual do Alcool é de R$1,90 por litro\nO preço atual da gasolina é de R$2,50 por litro'
      f'\nDesconto no Alcool até 20 litros - 3% - acima de 20 litros - 5%\n'
      f'Desconto na Gasolina até 20 litros - 4% - acimda de 20 litros - 6%')

tipo_combustivel = input("Digite A para álcool ou G para gasolina: ").upper()

if tipo_combustivel == "A":
    litros = float(input("Quantos litros deseja abastecer? "))
    if litros < 20:
        litros_pagar = litros*1.90 - (litros*0.03)
        print(f"Voce está abastacendo {litros}L de álcool e vai pagar R${round(litros_pagar,2)}")
    else:
        litros_pagar = litros*1.90 - (litros*0.05)
        print(f"Voce está abastacendo {litros}L de álcool e vai pagar R${round(litros_pagar,2)}")
else:
    litros = float(input("Quantos litros deseja abastecer? "))
    if litros < 20:
        litros_pagar = litros*2.50 - (litros*0.04)
        print(f"Voce está abastacendo {litros}L de gasolina e vai pagar R${round(litros_pagar,2)}")
    else:
        litros_pagar = litros*2.50 - (litros*0.06)
        print(f"Voce está abastacendo {litros}L de gasolina e vai pagar R${round(litros_pagar,2)}")
