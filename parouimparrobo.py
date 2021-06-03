from parouimparroboclass import Robo1, Robo2
import random
vitorias1 = 0
vitorias2 = 0
resultadosPar = 0
resultadosImpar = 0
for i in range(10):
    print('****************************************')
    print('Par ou Ímpar Robô')
    print('****************************************')
    robo1 = Robo1()
    robo1.imprime()
    print('******************************************')
    robo2 = Robo2(robo1)
    robo2.imprime()
    print('******************************************')

    print(f'O resultado é {robo1.escolha_numero + robo2.escolha_numero}')
    print('******************************************')

    if (robo1.escolha_numero + robo2.escolha_numero) % 2 == 0:
        resultadosPar += 1
        if robo1.escolha_parouimpar == 0:
            print('O resultado é um número par! O jogador 1 venceu!\n')
            vitorias1 += 1
        else:
            print('O resultado é um número par! O jogador 2 venceu!\n')
            vitorias2 += 1
    else:
        resultadosImpar += 1
        if robo1.escolha_parouimpar == 0:
            print('O resultado é um número ímpar! O jogador 2 venceu!\n')
            vitorias2 += 1
        else:
            print('O resultado é um número ímpar! O jogador 1 venceu!\n')
            vitorias1 += 1
print(f'O jogador 1 venceu {vitorias1} vezes')
print(f'O jogador 2 venceu {vitorias2} vezes\n')

print(f'O resultado foi par {resultadosPar} vezes')
print(f'O resultado foi ímpar {resultadosImpar} vezes')
