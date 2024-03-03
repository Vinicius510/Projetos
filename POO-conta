class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"O depósito de R${valor} foi realizado com sucesso!")
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"O valor de R${valor} foi sacado com sucesso!")
        else:
            print("Não foi possível sacar a quantia, saldo insuficiente")
            
    def obterSaldo(self):
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, titular, limite_cheque, saldo):
        super().__init__(titular, saldo)
        self.limite_cheque = limite_cheque
    
    def usar_cheque(self, valor):
        if self.saldo + self.limite_cheque >= valor:
            print(f"Usando cheque no valor de R${valor}")
        else:
            print("Limite excedido.")
            
c = Conta("vinicius", 1000)
c.depositar(500)
c.sacar(1000)
print("Saldo atual:", c.obterSaldo())
print("-------------------------------")
Cc = ContaCorrente("João", 500, 200)
Cc.depositar(800)
Cc.sacar(200)
print("Saldo atual:", Cc.obterSaldo())
Cc.usar_cheque(1000)
print("Saldo atual:", Cc.obterSaldo())
