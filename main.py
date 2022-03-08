from Conta import Conta, dicInvest, dicContaUser, dicContaAdm, Cartao, Premium
import re

# fazer menu para menu e sistema de login


def sacar(dicContaUser, auxtoken):
    valor = input()
    while valor is not int:
        valor = input("Digite um valor válido")
    conta = dicContaUser.get(auxtoken)
    if conta == None:
        auxtoken = input("Conta inválida, digite novamente!")
    conta.saque(valor)


def depositar(dicContaUser, auxtoken):
    valor = input()
    while valor is not int:
        input("Digite um valor válido")
    conta = dicContaUser.get(auxtoken)
    conta.deposito(valor)


def transfere(dicContaUser, auxtoken):
    valor = input()
    while valor is not int:
        input("Digite um valor válido")
    conta = dicContaUser.get(auxtoken)
    cod2 = input().strip
    conta2 = dicContaUser.get(cod2)
    conta.transfer(conta2, valor)


def extrato(dicContaUser, auxtoken):
    conta = dicContaUser.get(auxtoken)
    conta.extrato


def investe(dicContaUser, auxtoken):
    conta = dicContaUser.get(auxtoken)
    conta.investir()


def menuUser(hold):
    while True:
        print(
            "Bem vindo ao sistema! \nPara que eu possa ajudar digite qual serviço você procura:"
        )
        print(
            " 1 - Saque\n  - Depósito\n 3 - Transferência\n 4 - Extrato\n 5 - Investimento\n 6 - Sair"
        )
        hold = input().strip()
        while hold not in ["1", "2", "3", "4", "5", "6"]:
            hold = input("Digite um input válido").strip()
        hold = int(hold)
        if hold == 7:
            break

    oper = {
        1: sacar(),
        2: depositar(),
        3: transfere(),
        4: extrato(),
    }
    return oper.get(hold)


def menuPremium(hold):
    while True:
        print(
            "Bem vindo ao sistema! \nPara que eu possa ajudar digite qual serviço você procura:"
        )
        print(
            " 1 - Saque\n  - Depósito\n 3 - Transferência\n 4 - Extrato\n 5 - Investimento\n 6 - Sair"
        )
        hold = input().strip()
        while hold not in ["1", "2", "3", "4", "5", "6"]:
            hold = input("Digite um input válido").strip()
        hold = int(hold)
        if hold == 7:
            break
    oper = {
        1: sacar(),
        2: depositar(),
        3: transfere(),
        4: extrato(),
        5: investe(),
    }
    return oper.get(hold)


def menuAdm(hold):
    while True:
        print(
            "Bem vindo ao sistema! \nPara que eu possa ajudar digite qual serviço você procura:"
        )
        print(
            " 1 - Saque\n  - Depósito\n 3 - Transferência\n 4 - Extrato\n 5 - Investimento\n 6 - Sair"
        )
        hold = input().strip()
        while hold not in ["1", "2", "3", "4", "5", "6"]:
            hold = input("Digite um input válido").strip()
        hold = int(hold)
        if hold == 7:
            break

    oper = {
        1: sacar(),
        2: depositar(),
        3: transfere(),
        4: extrato(),
    }
    return oper.get(hold)


while True:
    aux = input("Você deseja logar como:\n 1.Usuario\n 2.Admin\n")
    if aux in "1":
        print("Bem vindo ao sistema! \nDigite Token e Senha\n ")
        auxtoken = int(input("Token: ").strip())
        auxpassword = input("Senha: ").strip()
        token2 = dicContaUser.get(auxtoken)
        if token2 == None:
            print("Token invalido")
        else:
            if auxpassword == token2.senha:
                if token2.Prem == 1:
                    menuPremium()
                else:
                    menuUser()
            else:
                print("Senha invalida")
                break
    ## if auxtoken not in dicContaUser or auxpassword not in dicContaUser:
    ##    print("Token ou senha invalido\n")
    elif aux in "2":
        print("Bem vindo ao sistema! \nDigite Token e Senha\n")
        auxtoken = int(input("Token: ").strip())
        auxpassword = input("Senha: ").strip()
        token2 = dicContaAdm.get(auxtoken)
        if token2 == None:
            print("Token invalido")
        else:
            if auxpassword == token2.senha:
                menuAdm()
            else:
                print("Senha invalida")
                break
        ####if auxtoken not in dicContaAdm or auxpassword not in dicContaAdm:
        ###print("Token ou senha invalido\n")
    else:
        aux = input("input invalido")
