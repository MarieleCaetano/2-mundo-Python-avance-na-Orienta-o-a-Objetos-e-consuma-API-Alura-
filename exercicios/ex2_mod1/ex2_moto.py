from ex2_veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)

        self._tipo = tipo


    
def __str__(self):
    status = "ligado" if self._ligado else "desligado"
    print('-'*30)
    return f"{self._marca} {self._modelo} - Tipo: {self._tipo} - Status: {status}"

