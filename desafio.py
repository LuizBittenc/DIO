menu = '''

[d] Despositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0.0
LIMITE_DIARIO = 500
dep = []
saque = []
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


def read_int(prompt, min, max):
    
    while True:
        
        try:
            valor = float(input(prompt))
            assert valor >= min and valor <= max
        except ValueError:
            print('Erro: o valor deve ser um numero')
        except AssertionError:
            print('Erro: o valor está fora do limite permitido R$ min - max')       
        except:
            pass
        else:
            return valor

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('Deposito')
        deposito = read_int('Qual o valor a depositar?', 1, 99999999999)
        dep.append(deposito)
        extrato.append(deposito)
        saldo = saldo  + deposito

    elif opcao == 's':
        print('Sacar')
        if numero_saques < LIMITE_SAQUES:
            saq = read_int('Qual o valor a Sacar?', 1, LIMITE_DIARIO)
            if saq <= saldo:
                saque.append(-saq)
                extrato.append(-saq)
                saldo = saldo - saq
                numero_saques += 1
            else:
                print('Saldo insuficiente para realizar este saque')
        else:
            print(f'Numero máximo de {LIMITE_SAQUES} saques por dia alcançado, tente sacar amanha.')

    elif opcao == 'e':
        print('Extrato')
        for item in extrato:
            if item > 0:
                x = f'Depósito:        R$ {item:.2f}'
                x = x.replace(',','')
                # x = x.replace('.',',').replace('_','.')  
            else:
                x = f'Saque:           R$ {item:.2f}'
                x = x.replace(',','')  
                # x = x.replace('.',',').replace('_','.')              
            print(x)
        print()
        print(f'Seu saldo é de: R$ {saldo:,.2f}')

    elif opcao == 'q':
        break

    else:
        print('Operecao invalida, por favor selecione novamente a operaçao desejada')