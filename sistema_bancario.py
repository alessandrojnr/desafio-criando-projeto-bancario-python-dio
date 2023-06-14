from time import sleep
def linha():
    print('-'*50)

menu = """  
    Bem vindo ao nosso sistema Bancário.
    Selecione a opção desejada:

        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair
        
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    linha()
    opcao = input(menu)
    sleep(1)

    if opcao == 'd':
        print("=== Depósito ===".center(50))
        deposito = float(input("\n  Informe a quantidade a depositar: "))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R$ {deposito:.2f}\n'
        else:
            print("Impossível realizar a operação. ")
        
    elif opcao == 's':
        print("=== Sacar ===".center(50))
        sacar = float(input("\n  Qual valor você gostaria de sacar : "))
        if sacar > saldo:
            print("Você não possui saldo suficiente.")
        elif sacar > limite:
            print("Valor inválido, o seu limite de saque é de R$ 500,00")
        elif LIMITE_SAQUES == 0:
            print("Você não tem limites para saque. Por favor utilizar a opção de saque em outro dia.")
        else:
            saldo -= sacar
            extrato += f'Saque : R$ {sacar:.2f}\n'
            LIMITE_SAQUES -= 1
            print(f'Você sacou R$ {sacar:.2f} e seu saldo atual é de R$ {saldo:.2f}')
        
    elif opcao == 'e':
        
        print("=== Extrato ===".center(50))
        print(extrato)
        print(f'\n  Seu Saldo é de R$ {saldo:.2f}, você ainda tem {LIMITE_SAQUES} limites para saque.')
        
    elif opcao == 'q':
        print("Saindo do sistema.")
        linha()
        break
    else:
        print('Por favor escolhar opção válida.')
      