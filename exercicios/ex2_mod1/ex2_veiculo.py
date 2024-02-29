class Veiculo:
    def __init__(self, marca, modelo):
    
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    def __str__(self):
        return f"Carro da marca: {self._marca}, modelo: {self._modelo} e status de ligado/desligado {self._ligado} "
    