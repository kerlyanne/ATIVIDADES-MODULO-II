from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def processar_pagamento(self):
        pass

class Cancelavel(ABC):
    @abstractmethod
    def cancelar_pagamento(self):
        pass

class CartaoCredito(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print("Pagamento processado via Cartão de Crédito.")

    def cancelar_pagamento(self):
        print("Pagamento cancelado (Cartão de Crédito).")

class Pix(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print("Pagamento processado via PIX.")

    def cancelar_pagamento(self):
        print("Pagamento cancelado (PIX).")

class Boleto(Pagamento, Cancelavel):
    def processar_pagamento(self):
        print("Pagamento processado via Boleto.")

    def cancelar_pagamento(self):
        print("Pagamento cancelado (Boleto).")