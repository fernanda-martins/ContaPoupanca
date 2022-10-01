class Conta:
    def __init__(self,**d):
        self.__numero = d['numero']
        self.saldo = d['saldo']
    def get_numero(self):
        return self.__numero
    def creditor(self,valor):
        self.saldo += valor
    def debitar(self,valor):
        self.saldo -= valor

class Poupanca(Conta):
    def __init__(self,**d):
        Conta.__init__(self,**d)
        self.rendimento = d['rendimento']
    def set_rendimento(self,taxa):
        self.rendimento += self.saldo * (taxa/100)

c1 = Conta(numero='52911-2',saldo=5000)
print(c1.get_numero(),c1.saldo)
c1.creditor(200)
print(c1.saldo)
c1.debitar(100)
print(c1.saldo)
p1 = Poupanca(numero=c1.get_numero(),saldo=c1.saldo,rendimento=0)
print(f'A conta {p1.get_numero()} é poupança e tem R${p1.saldo} com rendimento inicial de {p1.rendimento}%')
p1.set_rendimento(2)
print(f'O rendimento atual é {p1.rendimento}')
print(f'O montante final de saldo mais rendimento é {p1.saldo + p1.rendimento}')


