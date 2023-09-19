clientes = []
class Banco:

    def __init__ (self, nome_banc, saldo_banc):
        self.nome_banc = nome_banc
        self.saldo_banc = saldo_banc

    def criar_conta (self, nome_cliente, saldo_inicial_cliente):
        self.nome_cliente = nome_cliente
        self.saldo_inicial_cliente = saldo_inicial_cliente
        clientes.append(nome_cliente, saldo_inicial_cliente)

    def