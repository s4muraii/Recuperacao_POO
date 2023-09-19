from classes import *
import os

banco = Banco("Nubank", 50000)
while True:
    print ("------------------------------------------------\n\nBem vindo ao Sistema Bancário!\n\n------------------------------------------------\n\n ")
    menu = int(input("[1] - Criar conta\n[2] - Sacar\n[3] - Depositar\n[4] - Transferir\n[5]- Sair\n"))
    match menu:
        case 1:
            os.system("cls")
            cliente = Cliente (nome_cliente = input("Digite seu nome: "), saldo_inicial_cliente = float(input("Digite o saldo inicial da conta: ")))
            clientes.append(cliente)
            print("Cadastrado com sucesso!")
            os.system("pause")
            os.system("cls")

        case 2:
            print("Você escolheu sacar seu dinheiro! Certifique-se de ter saldo disponível.")
            banco.sacar(conta_saq = input("Digite o seu nome: "), valor_saq = float(input("Digite o valor a ser sacado")))
            os.system("pause")
            os.system("cls")
        
        case 3:
            print("Você escolheu depositar seu dinheiro!")
            banco.depositar(conta_dep = input("Digite seu nome: "), valor_dep = float(input("Digite o valor que deseja depositar: ")))

        case 4:
            print("Você escolheu transferir seu dinheiro!")
            banco.transferir(origem = input("Digite o nome da conta de origem: "), destino = input("Digite o nome da conta de destino: "), valor_transf = float(input("Digite o valor a ser transferido: ")))