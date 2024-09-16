class Conta:
    def __init__(self,numero_conta:int,agencia:int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0

    def depositar(self,valor):
        self._saldo += valor

    def sacar(self,valor):
        self._saldo -= valor