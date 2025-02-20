import os
import platform

def limpar_console():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

limpar_console()

saldo = 0
saques_do_dia = 0

extrato = {
    "depositos": [],
    "saques": [],
}

while True:
    respostas_possiveis = ["1" , "2" , "3", "4"]
    print("Bem vindo ao Banco!")
    print("")
    print("===> OPÇÕES <===")
    print("1 - Depositar \n2 - Sacar \n3 - Extrato \n4 - Sair")
    print("")
    resposta = input("O que deseja fazer?\nEscolha:")

    if resposta not in respostas_possiveis:
        print("Opção inválida")
        continue
    elif resposta == "1":
        limpar_console()
        try:
            valor = float(input("Digite o valor do depósito: "))
        except:
            print("Valor inválido.")
            continue
        if valor > 0:
            saldo+=valor
            extrato["depositos"].append(valor)
            print("Depósito realizado com sucesso.")
        else:
            print("Digite um valor maior.")

    elif resposta == "2":
        limpar_console()
        if saques_do_dia >= 3:
            print("Você já atingiu o limite de saques diários.")
            continue
        
        if saldo > 0:
            try:
                valor = float(input("Digite o valor do saque: "))
            except:
                print("Valor inválido.")
                continue

            if valor <= 500 and valor <= saldo:
                saldo-=valor
                saques_do_dia+=1
                extrato["saques"].append(valor)
                print("Saque realizado com sucesso.")
            else:
                print("Valor inválido.")
                continue
        else:
            print('Você não possui saldo.')
            continue
            
    elif resposta == "3":
        limpar_console()
        print("=========Extrato=========")
        print("")
        print("Depósitos:")
        for deposito in extrato["depositos"]:
            print(f"R$ {deposito:.2f}")
        print("")
        print("Saques:")
        for saque in extrato["saques"]:
            print(f"R$ {saque:.2f}")
        print("")
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif resposta == "4":
        print("")
        print("Obrigado por usar o Banco!")
        break
    print("============================================================================")