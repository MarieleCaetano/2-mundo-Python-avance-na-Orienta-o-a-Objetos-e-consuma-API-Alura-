class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    def dar_likes(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()
    
    def __str__(self):
        return f'{Programa._nome}, {Programa.ano}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome}, ano de lançamento: {self.ano}, duração: {self.duracao}, Likes: {self._likes}'

class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'Nome: {self._nome}, ano de lançamento: {self.ano}, temporadas: {self.temporadas}, Likes: {self._likes}'


crepusculo = Filme('Crepusculo', 2014, 1.45)
prince_dragon = Series('Prince Dragon',2018, 6)

crepusculo.dar_likes()
crepusculo.dar_likes()
crepusculo.dar_likes()

prince_dragon.dar_likes()
prince_dragon.dar_likes()

listinha = [crepusculo, prince_dragon]
for Programa in listinha:
    print(Programa)