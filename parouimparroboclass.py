import random

class Robo1:
    def __init__(self):
        print('Primeiro jogador irá jogar!\n')
        self.escolha_parouimpar = random.randint(0, 1)
        self.escolha_numero = random.randint(0, 999)

    def imprime(self):
        if self.escolha_parouimpar == 0:
            print('Ele escolheu par!')
        else:
            print('ELe escolheu ímpar!')
        print(f'Ele escolheu o número {self.escolha_numero}')

    pass

class Robo2:
    def __init__(self, robo1):
        print('O segundo jogador irá jogar!\n')
        if robo1.escolha_parouimpar == 0:
            self.escolha_parouimpar = 1
        else:
            self.escolha_parouimpar = 0
        self.escolha_numero = random.randint(0, 999)
    def imprime(self):
        if self.escolha_parouimpar == 0:
            print('Ele escolheu par!')
        else:
            print('Ele escolheu ímpar!')
        print(f'Ele escolheu o número {self.escolha_numero}')
    pass