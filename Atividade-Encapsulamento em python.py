class ContaBancaria:
    def __init__(self):
        self.__saldo = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("valor invalido para deposito.")
    
    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            print("saldo insuficiente.")
    
    def ver_saldo(self):
        return self.__saldo

conta = ContaBancaria()
conta.depositar(100)
conta.sacar(30)
print("Saldo atual:", conta.ver_saldo())


class Pessoa:
    def __init__(self, nome, anonasceu):
        self.__nome = nome
        self.__anonasceu = anonasceu

p = Pessoa("kerlyanne", 2000)
print(p._Pessoa__nome)
print(p._Pessoa__anonasceu)



class contabancaria:
    def __init__(self):
        self.__saldo = 0
    
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("o saldo nao pode ser negativo.")

c = contabancaria()
c.depositar(300)
print("saldo atual:", c.saldo())
c.depositar(-10)


class produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
    def nome(self):
        return self.__nome
    def preco(self):
        return self.__preco
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            print("preco nao pode ser negativo.")
            p=produto("celular",1500)
            print(p.nome)
            print(p.preco())
            p.preco=(1800)
            print(p.preco())
            p.preco=(-50)