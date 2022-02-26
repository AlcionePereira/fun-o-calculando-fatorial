'''lista-1 Q-4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação).'''

def mensagem():
    media = (nota1 + nota2) / 2
    if media > 6:
        print('PARABÉNS! você foi aprovado!')
    else:
        print('INFELIZMENTE! Você não foi aprovado!')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

mensagem()