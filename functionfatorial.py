
#Calaculando o fatorial de um número


def fatorial(x):
    print('Calculando o fatorial!')
    print(f'Calculando {n}!=', end='')


n = int(input('Digite um número para interiro: '))
contador = n
f = 1

while contador > 0:
    print(f'{contador}', end='')
    print('x' if contador > 1 else '=', end='')
    f *= contador
    contador -= 1
print(f)