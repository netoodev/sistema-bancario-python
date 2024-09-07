menu = """

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

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Não foi possível fazer o depósito. Valor informado é inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Não foi possível realizar a operação. Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Não foi possível realizar a operação. Valor do saque excedeu o limite.")

        elif excedeu_saques:
            print("Não foi possível realizar a operação. Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Não foi possível realizar a operação. Valor informado é inválido.")
            
    elif opcao == 'e':
        print("\n======================= EXTRATO =======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("======================================================")

    elif opcao == 'q':
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")