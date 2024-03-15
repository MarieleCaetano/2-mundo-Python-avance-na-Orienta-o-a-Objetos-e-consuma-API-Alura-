from livro import Livro

livro_biblioteca = Livro('Misery', 'stephen king', 1992)

print(f" {livro_biblioteca} \n Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
livro_biblioteca.emprestar()
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca.disponivel}")
ano_especifico = 2020

livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f'Livros disponiveis do ano de {ano_especifico}: {livros_disponiveis_ano}')
