# Início da função dimensoesObjeto
def dimensoesObjeto():
    while True:  # Início do laço para verificação de valores das dimensões
        try:
            com = int(input('Digite o comprimento do objeto (em cm):'))
            lar = int(input('Digite a largura do objeto (em cm):'))
            alt = int(input('Digite a altura do objeto (em cm):'))
            valor = float(com * lar * alt)
            res = valor
            print('Volume do objeto é (em cm³): {}'.format(res))
            if (res <= 999):
                return 10
            elif (res <= 10000):
                return 20
            elif (res <= 30000):
                return 30
            elif (res <= 100000):
                return 50
            else:
                print('Não aceitamos objetos com dimensões tão grandes! \n'
                      'Entre com as dimensões desejadas novamente')
                continue
        except ValueError:  # Comando para verificação de digitação
            print(
                'Você digitou alguma dimensão do objeto com valor não numérico! \n'
                'Por favor entre com as dimensões desejadas novamente')
            continue
# Fim da função dimensoesObjeto

# Início da função pesoObjeto
def pesoObjeto():
    while True:  # Início do laço para verificação de valores de peso
        try:
            peso = float(input('Digite o peso do objeto (em kg):'))
            kg = peso
            if (kg <= 0.1):
                return 1
            elif (kg <= 2):
                return 1.5
            elif (kg <= 9):
                return 2
            elif (kg <= 31):
                return 3
            else:
                print('Não aceitamos objetos tão pesados!')
                continue
        except ValueError:  # Comando para verificação de digitação
            print('Você digitou peso do objeto com valor não numérico! \n'
                  'Por favor entre com o peso desejado novamente')
            continue
# Fim da função pesoObjeto

# Início da função rotaObjeto
def rotaObjeto():
    while True:  # Início do laço para verificação de valores das rotas
        try:
            rota = (input(
                'Selecione a rota: \n'
                'BR - De Brasília para Rio de Janeiro\n'
                'BS - De Brasília para São Paulo\n'
                'RB - De Rio de Janeiro para Brasília\n'
                'RS - De Rio de Janeiro para São Paulo\n'
                'SR - De São Paulo para Rio de Janeiro\n'
                'SB - De São Paulo para Brasília\n >>'))
            rota = rota.upper()  # Comando caso o usuário digite em minúsculo
            trajeto = rota
            if (trajeto == 'RS'):
                return 1
            elif (trajeto == 'SR'):
                return 1
            elif (trajeto == 'BS'):
                return 1.2
            elif (trajeto == 'SB'):
                return 1.2
            elif (trajeto == 'BR'):
                return 1.5
            elif (trajeto == 'RB'):
                return 1.5
            else:
                print('Você digitou uma rota que não existe!')
                continue
        except ValueError:  # Comando para verificação de digitação
            print('Você digitou uma rota que não existe!\n'
                  'Por favor entre com a rota desejada novamente')
            continue
# Fim da função rotaObjeto

# Início do programa principal
print('Bem vindo a companhia de logistica Sheila Hui Yi Chiu RU:4412400')
dim = dimensoesObjeto()
peso = pesoObjeto()
rot = rotaObjeto()
print('Total a pagar(R$): {:.2f} (Dimensões: {} * Peso: {} * Rota: {})'.format(dim * peso * rot, dim, peso, rot))
# Resposta e cálculo feito
# Fim do programa principal