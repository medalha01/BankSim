from audioop import adpcm2lin
import secrets

dicInvest = {}
dicContaAdm = {}
dicContaUser = {}
dicContaPr = {}


class Conta:
    def __init__(self, Cpf, Nome, Senha, Saldo):
        self.Token = secrets.token_bytes(16)
        self.cpf = Cpf
        self.senha = Senha
        self.nome = Nome
        self.saldo = Saldo
        self.historico = ()

    def deposito(self, valor):
        self.saldo = self.saldo + valor
        self.historico.append("+ {}".format(valor))

    def saque(self, valor):
        if self.saldo > valor:
            self.saldo = self.saldo - valor
            self.historico.append("- {}".format(valor))
        else:
            print("Saldo Insuficiente")

    def extrato(self):
        print("Seu Saldo é de:", self.saldo, "\n")
        print(self.historico)

    def transfer(self, destino, valor):
        if self.saldo > valor:
            self.saldo = self.saldo - valor
            destino.saldo = destino.saldo + valor
            self.historico.append("Transferencia para {destino}: - {valor}")
            destino.historico.append("Transferencia recebido {self}: + {valor}")


class Cartao(Conta):
    def __init__(self, Limite_trans, Numero_card, Codigo_seg, Senha_card):
        self.limite_trans = Limite_trans
        self.numero_card = Numero_card
        self.codigo_seg = Codigo_seg
        self.senha_card = Senha_card

    # def Compra():


# Pedir senha para todo uso do cartão


class Admin(Conta):
    def __init__(self, Nome, Senha, Cpf):
        Conta.__init__(self, Cpf, Nome, Senha)

    def saldoMod(self, conta, valor):
        # pegar codigo e valor no main
        # transformar em int
        print("Digite sua senha para realizar a operação:")
        senha2 = input().strip
        if self.Senha == senha2:
            conta.saldo = conta.saldo + valor

    def creatUser(self, tipo):
        # fazer escolha de tipo no main
        administrador = ("admin", "administrador", "adm")
        premium = "premium, pr, prmium, pre, especial, completa"
        conta = ("conta", "normal", " ", "")
        ct = secrets.token_bytes(20)
        if tipo.lower() in administrador:
            i1 = "Qual o nome do dono da conta?"
            i2 = "Qual o cpf do dona da conta?"
            i3 = "Qual a senha da conta?"
            contaadm = Admin(i1, i3, i2)
            print(f"Este é o token de sua conta {ct}")
            dicContaAdm.update({ct: contaadm})
        elif tipo.lower() in premium:
            fnfusdhbfsuf = 1
        elif tipo.lower() in conta:
            fnfusdhbfsuf = 1


class Premium(Conta):
    def __init__(self, Cpf, Nome, Senha, Saldo, Carteira):
        Conta.__init__(self, Cpf, Nome, Senha, Saldo)
        self.Carteira = Carteira()

    def investir(self):
        print(dicInvest)
        nome = input("Selecione o investimento")
        investimento = dicInvest.get(nome)
        Quant = input("Quanto deseja investir?")
        while Quant > self.Saldo:
            Quant = input("Digite uma quantia valida!")
        if Quant < investimento.custo:
            print(
                "O valor de entrada é maior que a quantidade desejada que seja investido."
            )
        else:
            invest2 = (nome, Quant)
            # adicionar depois um sistema de check para caso investimento já exista
            self.carteira.append(invest2)
            self.Saldo = self.Saldo - Quant


class invest(Premium):
    def __init__(self, duration, juros, tipo, custo, mtime):
        self.duration = duration
        self.juros = juros
        self.tipo = tipo
        self.custo = custo
        self.mtime = mtime

    def investCreation(self):
        self.nome = input("Digite o nome do investimento:")
        self.duration = input("Digite a duração máxima do investimento:")
        self.juros = input("Digite os juros:")
        self.tipo = input("Digite o tipo de investimento:")
        self.custo = input("Digite o custo de entrada:")
        self.mtime = input("Digite o tempo minimo para retirada:")
        dicInvest.update({self.nome: self})
        # Pedir que seja admin no main para conseguir criar um investimento

    def interestrate(self, valor):
        pagamento = valor * self.juros
        return pagamento
        ###fazer o sistema de pagamento no main###
