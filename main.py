from Conta import Conta, dicInvest, dicContaUser, dicContaAdm, Cartao, Premium, dicCard
import re

# fazer menu para menu e sistema de login
# python talvez tenha alguma lib facil de usar de sqlite


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


# fazer
def criarCartao(auxtoken):
    auxtoken


def menuUser(auxtoken):
    while True:
        print(
            "Bem vindo ao sistema! \nPara que eu possa ajudar digite qual serviço você procura:"
        )
        print(
            " 1 - Saque\n  2 - Depósito\n 3 - Transferência\n 4 - Extrato\n 5 - Criar Cartão \n 6 - Sair"
        )
        hold = input().strip()
        while hold not in ["1", "2", "3", "4", "5", "6"]:
            hold = input("Digite um input válido").strip()
        hold = int(hold)
        if hold == 6:
            break

    oper = {
        1: sacar(auxtoken),
        2: depositar(auxtoken),
        3: transfere(auxtoken),
        4: extrato(auxtoken),
        5: criarCartao(auxtoken),
    }
    func = oper.get(hold)
    func


def menuPremium(auxtoken):
    while True:
        print(
            "Bem vindo ao sistema! \nPara que eu possa ajudar digite qual serviço você procura:"
        )
        print(
            " 1 - Saque\n  2 - Depósito\n 3 - Transferência\n 4 - Extrato\n 5 - Criar Cartão \n 6 - Investir \n 7 - Sair"
        )
        hold = input().strip()
        while hold not in ["1", "2", "3", "4", "5", "6", "7"]:
            hold = input("Digite um input válido").strip()
        hold = int(hold)
        if hold == 7:
            break

    oper = {
        1: sacar(auxtoken),
        2: depositar(auxtoken),
        3: transfere(auxtoken),
        4: extrato(auxtoken),
        5: criarCartao(auxtoken),
        6: investe(auxtoken)
    }
    func = oper.get(hold)
    func


def menuAdm(hold):
    while True:
        print(
            "Bem vindo ao sistema! \nPara que eu possa ajudar digite qual serviço você procura:"
        )
        print(
            " 1 - Criar Conta\n 2 - Criar Investimento \n 3 - Deletar Conta \n 4 - Modificar saldo\n 5 - Pagar Juros\n 6 - Sair"
        )
        hold = input().strip()
        while hold not in ["1", "2", "3", "4", "5", "6"]:
            hold = input("Digite um input válido").strip()
        hold = int(hold)
        if hold == 6:
            break
##arumar oper
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
                    menuPremium(auxtoken)
                else:
                    menuUser(auxtoken)
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
                menuAdm(auxtoken)
            else:
                print("Senha invalida")
                break
        ####if auxtoken not in dicContaAdm or auxpassword not in dicContaAdm:
        ###print("Token ou senha invalido\n")
    else:
        aux = input("input invalido")
