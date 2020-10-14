# Exercicio 11

salario = float(input('Informe seu salario: '))
novo_salario = 0

if salario <= 280:
    reajuste = (salario * 0.20)
    novo_salario = salario + reajuste
    print(f'Salario antes do reajuste R%{salario:.2f}\nSalario após o reajuste R${novo_salario:.2f}\nPercentual de aumento 20%\nValor do aumento {salario * 0.20:.2f}')
elif 280 < salario <= 700:
    reajuste = (salario * 0.15)
    novo_salario = salario + reajuste
    print(f'Salario antes do reajuste R%{salario:.2f}\nSalario após o reajuste R${novo_salario:.2f}\nPercentual de aumento 15%\nValor do aumento {salario * 0.20:.2f}')
elif 700 < salario > 1500:
    reajuste = (salario * 0.05)
    novo_salario = salario + reajuste
    print(f'Salario antes do reajuste R%{salario:.2f}\nSalario após o reajuste R${novo_salario:.2f}\nPercentual de aumento 5%\nValor do aumento {salario * 0.20:.2f}')
