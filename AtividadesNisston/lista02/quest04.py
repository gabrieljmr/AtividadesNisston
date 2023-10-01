class ContaBancaria:
    def __init__ (self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo


conta1 = ContaBancaria(500, "João")

print(conta1.saldo, conta1.titular)