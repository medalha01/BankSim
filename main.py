from Conta import (
    Conta,
    dicInvest,
    dicContaUser,
    dicContaAdm,
    Cartao,
    Premium,
    dicCard,
    Admin,
    invest,
)
import re, random

mainadm = Admin("Nome", "Senha", "Cpf", 123)
dicContaAdm.update({123: mainadm})
# fazer menu para menu e sistema de login
# python talvez tenha alguma lib facil de usar de sqlite

##"    1: accountCreate(),2: investCreate(),3: deleteAccount(), 4: modify(), 5: payinterest(),###
def accountCreate(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    pool = ["admin", "normal", "premium"]
    print(f"Qual tipo de conta você deseja criar? \n {pool}")
    adm = dicContaAdm.get(auxtoken)
    tipo = input()
    while tipo not in pool:
        tipo = input("Tente novamente")
    adm.creatUser(tipo)


def investCreate(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    adm = dicContaAdm.get(auxtoken)
    adm.investCreation()


def deleteAccount(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    tokenalvo = input(("qual a conta(token) que será deletada?\n "))
    dicContaUser.pop(tokenalvo)


def modify(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    adm = dicContaAdm.get(auxtoken)
    conta = input(("qual a conta(token) que será modificada?\n "))
    print("em quantos será alterado o saldo?\n")
    valor = float(input())
    adm.saldoMod(conta, valor)


def payInterest(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    investname = input("digite o investimento")
    while investname not in dicInvest:
        investname = input("digite investimento valido")
    aux = dicInvest.get(investname)
    aux.intestrate(investname)


def sacar(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    valor = input()
    while valor is not int:
        valor = input("Digite um valor válido")
    conta = dicContaUser.get(auxtoken)
    if conta == None:
        auxtoken = input("Conta inválida, digite novamente!")
    conta.saque(valor)


def depositar(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    valor = input()
    while valor is not int:
        input("Digite um valor válido")
    conta = dicContaUser.get(auxtoken)
    conta.deposito(valor)


def transfere(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    valor = input()
    while valor is not int:
        input("Digite um valor válido")
    conta = dicContaUser.get(auxtoken)
    cod2 = input().strip
    conta2 = dicContaUser.get(cod2)
    conta.transfer(conta2, valor)


def extrato(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    conta = dicContaUser.get(auxtoken)
    conta.extrato


def investe(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    conta = dicContaUser.get(auxtoken)
    conta.investir()


# feito
def criarCartao(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm):
    #    def __init__(self, Limite_trans, Numero_card, Codigo_seg, Senha_card, Token):
    j1 = input("Qual o limite do cartão?")
    j2 = (
        str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
        + str(random.randrange(9))
    )
    j3 = str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9))
    j4 = input("Digite a senha do cartão")
    Token = auxtoken
    Cartao = Cartao(j1, j2, j3, j4, Token)
    dicCard.update({Token: Cartao})


def menuUser(auxtoken):
    while True:
        oper = {
        1: sacar,
        2: depositar,
        3: transfere,
        4: extrato,
        5: criarCartao,
        }
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
        return oper.get(hold)


def menuPremium(auxtoken):

    while True:
        oper = {
        1: sacar,
        2: depositar,
        3: transfere,
        4: extrato,
        5: criarCartao,
        6: investe,
        }
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
        return oper.get(hold)


def menuAdm(auxtoken):
    
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
        oper = {
        1: accountCreate,
        2: investCreate,
        3: deleteAccount,
        4: modify,
        5: payInterest,
        }
        if hold == 6:
            break
        return oper.get(hold)
    ##arumar oper


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
                    x = menuPremium(auxtoken)
                    x(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm)
                else:
                    x = menuUser(auxtoken)
                    x(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm)
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
                x = menuAdm(auxtoken)
                x(auxtoken, dicCard, dicInvest, dicContaUser, dicContaAdm)
            else:
                print("Senha invalida")
                break
        ####if auxtoken not in dicContaAdm or auxpassword not in dicContaAdm:
        ###print("Token ou senha invalido\n")
    else:
        aux = input("input invalido")
