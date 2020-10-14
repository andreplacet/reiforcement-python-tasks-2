# Exercicio 21

saque = int(input("Quanto voce deseja sacar? o minumo é R$10 reais e máximo é R$600 reais: "))

if saque < 10 or saque > 600:
    print("Valor invalido, reinicie a operação com um valor válido")
else:
    cem_reais = saque // 100 #cédulas de 100 reais
    saque = saque - (cem_reais*100)
    cinquenta_reais = saque // 50
    saque = saque - (cinquenta_reais*50)
    dez_reais = saque // 10
    saque = saque - (dez_reais*10)
    cinco_reais = saque // 5
    saque = saque - (cinco_reais*5)
    um_real = saque // 1
    saque = saque - (um_real*100)
    print(f"""    Notas de R$100 = {cem_reais}
    Notas de R$50,00 = {cinquenta_reais}
    Notas de R$10,00 = {dez_reais}
    Notas de R$5,00 = {cinco_reais}
    Nota de R$1,00 = {um_real}""")
