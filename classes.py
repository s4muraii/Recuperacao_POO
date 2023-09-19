clientes = []
class Banco:

    def __init__ (self, nome_banc, saldo_banc):
        self.nome_banc = nome_banc
        self.saldo_banc = saldo_banc

class Cliente (Banco):
    def __init__ (self, nome_cliente, saldo_inicial_cliente):
        self.nome_cliente = nome_cliente
        self.saldo_inicial_cliente = saldo_inicial_cliente

    def getClientenome(self):
        return self.nome_cliente
    
    def getClienteSaldo(self):
        return self.saldo_inicial_cliente
    
    def setClienteSaldo(self, novosaldo):
        self.saldo_inicial_cliente = novosaldo
    
    def sacar(self, conta_saq, valor_saq):
        self.conta_saq = conta_saq

        self.valor_saq = valor_saq
        if self.saldo_inicial_cliente >= valor_saq:
            self.saldo_inicial_cliente = (self.saldo_inicial_cliente) - (valor_saq)
            print("Saque realizado com sucesso!")
        else:
            print("Você não possui saldo disonível!")
    def depositar(self, conta_dep, valor_dep):
        self.conta_dep = conta_dep

        self.valor_dep = valor_dep
        self.saldo_inicial_cliente = (self.saldo_inicial_cliente) + (valor_dep)
        print (f"Depósito realizado com sucesso! Você depositou {valor_dep} reais")

    def transferir (self, destino, valor_transf):
        self.destino = destino
        self.valor_transf = valor_transf

    
    def getTransfDestino(self):
        return self.destino
    
    def getTransfValor(self):
        return self.valor_transf