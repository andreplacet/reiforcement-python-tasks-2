# Exercicio 12

ir = 0.05
inss = 0.10
fgts = 0.11
sindicato = 0.03

valor_hora = float(input('Informe o valor cobrado por hora: '))
horas_trabalhadas = float(input('Informe quantas horas trabalhadas: '))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    total_descontos = (salario_bruto * sindicato) + (salario_bruto * inss)
    salario_liquido = salario_bruto - total_descontos
    print(f'Salario bruto R${salario_bruto:.2f}\nIR: ISENTO\nINSS R${salario_bruto * inss:.2f}\n'
          f'FGTS R${salario_bruto * fgts:.2f}\nTotal dos descontos R${total_descontos:.2f}\n'
          f'Salario Liquido R${salario_liquido:.2f}')
elif 900 < salario_bruto <= 1500:
    total_descontos = (salario_bruto * sindicato) + (salario_bruto * ir) + (salario_bruto * inss)
    salario_liquido = salario_bruto - total_descontos
    print(
        f'Salario bruto R${salario_bruto:.2f}\nIR: R${salario_bruto * ir:.2f}\nINSS R${salario_bruto * inss:.2f}\n'
        f'FGTS R${salario_bruto * fgts:.2f}\nTotal dos descontos R${total_descontos:.2f}\n'
        f'Salario Liquido R${salario_liquido:.2f}')
elif 1500 < salario_bruto <= 2500:
    ir = 0.10
    total_descontos = (salario_bruto * sindicato) + (salario_bruto * ir) + (salario_bruto * inss)
    salario_liquido = salario_bruto - total_descontos
    print(
        f'Salario bruto R${salario_bruto:.2f}\nIR: R${salario_bruto * ir:.2f}\nINSS R${salario_bruto * inss:.2f}\n'
        f'FGTS R${salario_bruto * fgts:.2f}\nTotal dos descontos R${total_descontos:.2f}\n'
        f'Salario Liquido R${salario_liquido:.2f}')
else:
    ir = 0.20
    total_descontos = (salario_bruto * sindicato) + (salario_bruto * ir) + (salario_bruto * inss)
    salario_liquido = salario_bruto - total_descontos
    print(
        f'Salario bruto R${salario_bruto:.2f}\nIR: R${salario_bruto * ir:.2f}\nINSS R${salario_bruto * inss:.2f}\n'
        f'FGTS R${salario_bruto * fgts:.2f}\nTotal dos descontos R${total_descontos:.2f}\n'
        f'Salario Liquido R${salario_liquido:.2f}')
