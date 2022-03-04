def poligono():
    if n_lados == 3:
        perimetro = medida_lado * 3
        print(f'O polígono é um TRIÂNGULO de perímetro {perimetro}')
    elif n_lados == 4:
        perimetro = medida_lado * 4
        print(f'O polígono é um QUADRADO de perímetro {perimetro}')
    else:
        perimetro = medida_lado * 5
        print(f'O polígono é um PENTÂGONO de perimetro {perimetro}')
        poligono = ''


while True:
    n_lados = int(input('Digite a quantidade de lados: '))
    if n_lados == 3 or n_lados == 4 or n_lados == 5:
        medida_lado = int(input('Digite a medida dos lados: '))
        break
    else:
        print('ERRO! Você não digitou um número entre 3 e 5:')

poligono()
