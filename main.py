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

mainadm = Admin("Nome", "Senha", "Cpf")
dicContaAdm.update({123: mainadm})
# fazer menu para menu e sistema de login
# python talvez tenha alguma lib facil de usar de sqlite

##"    1: accountCreate(),2: investCreate(),3: deleteAccount(), 4: modify(), 5: payinterest(),###
def accountCreate(auxtoken):
    pool = ["admin", "normal", "premium"]
    print(f"Qual tipo de conta você deseja criar? \n {pool}")
    adm = dicContaAdm.get(auxtoken)
    tipo = input()
    while tipo not in pool:
        tipo = input("Tente novamente")
    adm.creatUser(tipo)


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


# feito
def criarCartao(auxtoken):
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
    oper = {
        1: sacar(auxtoken),
        2: depositar(auxtoken),
        3: transfere(auxtoken),
        4: extrato(auxtoken),
        5: criarCartao(auxtoken),
    }


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
        return oper.get(hold)
    oper = {
        1: sacar(auxtoken),
        2: depositar(auxtoken),
        3: transfere(auxtoken),
        4: extrato(auxtoken),
        5: criarCartao(auxtoken),
        6: investe(auxtoken),
    }


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
        return oper.get(hold)
    ##arumar oper
    oper = {
        1: accountCreate(auxtoken),
        2: investCreate(),
        3: deleteAccount(),
        4: modify(),
        5: payinterest(),
    }


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
