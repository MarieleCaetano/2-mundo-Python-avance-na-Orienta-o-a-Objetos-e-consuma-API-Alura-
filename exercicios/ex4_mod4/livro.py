
class Livro:
    def __init__(self, titulo, autor, ano_de_publicação):
        self._titulo = titulo
        self._autor = autor
        self._ano_de_publicação = ano_de_publicação
        self.disponivel = True
    
    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano da publicação: {self._ano_de_publicação}'

    def emprestar(self):
        self.disponivel = False
    
    
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_de_publicação == ano and livro.disponivel]
        def __str__ ():
            return livros_disponiveis
    

livro_3 = Livro("Python Cookbook", "Samuel Developer", 2019)
livro_1 = Livro('Golen e o gênio', 'Wenecker', 2020)
livro_2 = Livro('Ladrão de almas', 'Alma Katsu', 2010)
Livro.livros = [livro_1, livro_2, livro_3]

print(livro_1)
print(livro_2)
