clientes = []
class Banco:

    def __init__ (self, nome_banc, saldo_banc):
        self.nome_banc = nome_banc
        self.saldo_banc = saldo_banc

    def criar_conta (self, nome_cliente, saldo_inicial_cliente):
        self.nome_cliente = nome_cliente
        self.saldo_inicial_cliente = saldo_inicial_cliente
        clientes.append(nome_cliente, saldo_inicial_cliente)
        return saldo_inicial_cliente
    
    def getClientenome(self):
        return self.nome_cliente
    
    def getClienteSaldo(self):
        return self.saldo_inicial_cliente
    
    def sacar(self, conta_saq, valor_saq):
        self.conta_saq = conta_saq
        conta_saq = input("Digite a conta desejada: ")

        self.valor_saq = valor_saq
        valor_saq = input("Digite o valor que deseja sacar: ")
        saldo_inicial_cliente = (saldo_inicial_cliente) - (valor_saq)

    def depositar(self, conta_dep, valor_dep):
        self.conta_dep = conta_dep
        conta_dep = input("Digite a conta desejada: ")

        self.valor_dep = valor_dep
        saldo_inicial_cliente = (saldo_inicial_cliente) + (valor_dep)

    def transferir (self, origem, destino, valor_transf):
        self.origem = origem
        self.destino = destino
        self.valor_transf = valor_transf

        origem = input("Digite a conta de origem: ")
        destino = input("Digite a conta destino: ")
        valor_transf = float(input("Digite o valor desejado: "))