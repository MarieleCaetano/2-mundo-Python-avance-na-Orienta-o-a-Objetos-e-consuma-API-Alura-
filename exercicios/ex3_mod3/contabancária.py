class ContabancariaPythonica:
    def __init__(self, titular, saldo, ativo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = ativo

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo



    def __str__(self):
        if self.ativo == False:
            return f'Titular da conta: {self._titular} e saldo: {self._saldo} e conta está INATIVA '
        elif self.ativo == True:
            return f'Titular da conta: {self._titular} e saldo: {self._saldo} e conta está ATIVA '

        
conta1 = ContabancariaPythonica('Anabeth', 1.234, False)
conta2 = ContabancariaPythonica('Marlon', 879, True)

print(f'Titular da conta 1: {conta1.titular}')
print(f'Titular da conta 2: {conta2.titular}')