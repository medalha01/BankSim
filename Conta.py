import secrets

# atualizar listas, dicionarios em operações,fazer menu, terminar cartão, sistema de arquivo, saldomod
dicInvest = {}
dicContaAdm = {}
dicContaUser = {}
dicCard = {}
listCardHist = []
##Pegar contas do dicionario e devolver elas, nunca chamar aleatoriamente
class Conta:
    def __init__(self, Cpf, Nome, Senha, Saldo, Token):
        self.cpf = Cpf
        self.senha = Senha
        self.nome = Nome
        self.saldo = Saldo
        self.historico = []
        self.Prem = 0
        self.token = Token

    def deposito(self, valor):
        self.saldo = float(self.saldo) + float(valor)
        self.historico.append("+ {}".format(valor))
        dicContaUser.update({self.token: self})
        print(f"Seu Saldo é de:{self.saldo}\n")

    def saque(self, valor):
        if float(self.saldo) >= float(valor):
            self.saldo = float(self.saldo) - valor
            self.historico.append("- {}".format(valor))
            dicContaUser.update({self.token: self})
            print(f"Seu Saldo é de:{self.saldo}\n")
        else:
            print("Saldo Insuficiente")

    def extrato(self):
        print(f"Seu Saldo é de:{self.saldo}\n")
        print(self.historico)

    def transfer(self, destino, valor):
        if float(self.saldo) >= float(valor):
            destino = dicContaUser.get(destino)
            self.saldo = float(self.saldo) - float(valor)
            destino.saldo = float(destino.saldo) + float(valor)
            dicContaUser.update({self.token: self})
            dicContaUser.update({destino.token: destino})
            self.historico.append("Transferencia para {destino}: - {valor}")
            destino.historico.append("Transferencia recebido {self}: + {valor}")
            print(f"Seu Saldo é de:{self.saldo}\n")

    def mudarsenha(self):
        l = input("Qual a nova senha que você deseja?").strip()
        self.senha = l
        print(f"Senha atualizada, sua nova senha agora é {l}")
        dicContaUser.update({self.token: self})

    # def CriarCard():#


class Cartao:
    def __init__(self, Limite_trans, Numero_card, Codigo_seg, Senha_card, Token):
        self.limite_trans = Limite_trans
        self.numero_card = Numero_card
        self.codigo_seg = Codigo_seg
        self.senha_card = Senha_card
        self.token = Token
        self.block = 0

    def Compra(self, valor):
        if self.block == 1:
            print("Cartão bloqueado, desbloqueie para efetuar transação")
        else:
            if float(self.saldo) >= float(valor):
                self.saldo -= float(valor)
                self.historico.append(
                    "Transação realizada {self.numero_card}: + {valor}"
                )
                dicContaUser.update({self.Token: self})
                listCardHist.append(self.Numero_card, self.historico)
            else:
                print("Saldo insuficiente")

    def Bloquear(self):
        x = input("Deseja bloquear o Cartão? (S/N)").lower()
        while x not in ("sim", "nao", "não", "n", "s"):
            x = input("Deseja bloquear o Cartão? (S/N)").lower()
        if x in ("sim", "s"):
            self.block = 1
        else:
            self.block = 0


class transactions(Cartao):
    def __init__(self, Limite_trans, Numero_card, Codigo_seg, Senha_card, Token):
        Conta.__init__(self, Limite_trans, Numero_card, Codigo_seg, Senha_card, Token)
        self.historico = []


# Pedir senha para todo uso do cartão


class Admin(Conta):
    def __init__(self, Nome, Senha, Cpf, Token):
        Conta.__init__(self, Cpf, Nome, Senha, 0, Token)

    def saldoMod(self, conta, valor):
        # pegar codigo e valor no main
        # transformar em int
        senha2 = input("Digite senha para realizar a operação:").strip()
        if self.senha == senha2:
            alvo = dicContaUser.get(conta)
            while alvo.saldo + valor < 0:
                valor = float(input("digite um valor valido de operação:\n"))
            alvo.saldo = float(alvo.saldo) + float(valor)
            dicContaUser.update({alvo.token: alvo})
        else:
            senha2 = input("senha invalida, encerrando operação.").strip()

    def investCreation(self):
        nome = input("Digite o nome do investimento:")
        duration = int(input("Digite a duração máxima do investimento:"))
        juros = float(input("Digite os juros:"))
        tipo = input("Digite o tipo de investimento:")
        custo = float(input("Digite o custo de entrada:"))
        mtime = int(input("Digite o tempo minimo para retirada:"))
        investimento = invest(duration, juros, tipo, custo, mtime)
        dicInvest.update({nome: investimento})

    def creatUser(self, tipo):
        # fazer escolha de tipo no main
        administrador = ("admin", "administrador", "adm")
        premium = "premium, pr, prmium, pre, especial, completa"
        conta = ("conta", "normal", " ", "")
        ct = secrets.token_bytes(20)
        ct = str(ct)
        if tipo.lower() in administrador:
            i1 = input("Qual o nome do dono da conta?")
            i2 = input("Qual o cpf do dona da conta?")
            i3 = input("Qual a senha da conta?")
            contaadm = Admin(i1, i3, i2, ct)
            print(f"Este é o token de sua conta {ct}")
            dicContaAdm.update({ct: contaadm})
        elif tipo.lower() in premium:
            # Cpf, Nome, Senha, Saldo, Carteira
            # sistema de validação no main
            i1 = input("Qual o cpf do dono da conta?")
            i2 = input("Qual o Nome do dona da conta?")
            i3 = input("Qual a senha da conta?")
            i4 = float(input("Qual o saldo inicial da conta?"))
            contapr = Premium(i1, i2, i3, i4, ct)
            print(f"Este é o token de sua conta {ct}")
            dicContaUser.update({ct: contapr})
        elif tipo.lower() in conta:
            i1 = input("Qual o cpf do dono da conta?")
            i2 = input("Qual o Nome do dona da conta?")
            i3 = input("Qual a senha da conta?")
            i4 = float(input("Qual o saldo inicial da conta?"))
            contaUser = Conta(i1, i2, i3, i4, ct)
            print(f"Este é o token de sua conta {ct}")
            dicContaUser.update({ct: contaUser})


##Fazer atualização da "investir"
class Premium(Conta):
    def __init__(self, Cpf, Nome, Senha, Saldo, Token):
        Conta.__init__(self, Cpf, Nome, Senha, Saldo, Token)
        self.Carteira = {}
        self.Prem = 1
        
    def extrato(self):
        print(f"Seu Saldo é de:{self.saldo}\n")
        print(self.historico)
        print(f"Sua carteira é {self.Carteira}\n")
        
    def investir(self):
        print(dicInvest)
        nome = input("Selecione o investimento: ")
        while nome not in dicInvest:
            nome = input("Selecione um investimento valido: ")
        investimento = dicInvest.get(nome)
        Quant = float(input("Quanto deseja investir?"))
        while Quant > self.saldo:
            Quant = float(input("Digite uma quantia valida!"))
        if Quant < investimento.custo:
            print(
                "O valor de entrada é maior que a quantidade desejada que seja investido."
            )
        else:
            invest2 = {nome: Quant}
            hold = self.Carteira.get(nome)
            if hold == None:
                self.Carteira.update(invest2)
                self.saldo = self.saldo - Quant
                print(f"Seu Saldo é de:{self.saldo}\n")

            else:
                hold = hold + Quant
                self.Carteira.update({nome: hold})
                self.saldo = self.saldo - Quant
                print(f"Seu Saldo é de:{self.saldo}\n")



class invest(Premium):
    def __init__(self, duration, juros, tipo, custo, mtime):
        self.duration = duration
        self.juros = juros
        self.tipo = tipo
        self.custo = custo
        self.mtime = mtime

        # Pedir que seja admin no main para conseguir criar um investimento

    def interestrate(self, investname):
        for x in dicContaUser.values():
            if x.Prem == 1:
                carteira = x.Carteira
                tokenalvo = x.token
                for i in carteira.keys():
                    if investname == i:
                        valor = carteira.get(investname)
                        valor = float(valor)
                        pagamento = valor * self.juros
                        x.saldo += pagamento
                        dicContaUser.update({tokenalvo: x})

        ###fazer o sistema de pagamento no main###
