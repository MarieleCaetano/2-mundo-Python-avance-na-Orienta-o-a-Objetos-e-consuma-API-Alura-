class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
    
    @property
    def likes(self):
        return self.__likes
    
    def dar_like(self):
        self.__likes += 1

crespusculo = Filme('Crepusculo', 2012, 130)
blade_runner = Filme('Blade Runner', 2018, 159)

print(f'''Nome dos filmes: {crespusculo.nome}, {blade_runner.nome}. Ano de lançamento: {crespusculo.ano},
{blade_runner.ano}. Duração {crespusculo.duracao} minutos e {blade_runner.duracao} minutos''')