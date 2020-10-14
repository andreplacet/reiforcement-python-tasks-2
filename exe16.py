# Exercicio 16

import math

print('Equaçao do 2o grau: ax² + bx + c')

a = int(input('Coeficiente [a]: '))

if a == 0:
    print('Se a = 0, não é equação do segundo grau')
else:
    b = int(input('Coeficiente b: '))
    c = int(input('Coeficiente c: '))
    delta = b * b - (4 * a * c)

    if delta < 0:
        print('Delta menor que 0')
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f'Delta = 0 , raiz = {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Raizes: {raiz1} e {raiz2}')
