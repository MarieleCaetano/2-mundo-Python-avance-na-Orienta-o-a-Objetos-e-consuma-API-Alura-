from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco = preco
        

# classe abstrata não é uma classe que quero que a classe Item cardapio instancie ou q ela faça alguma 
# coisa o que a classe abstrata faz é algo que serve de exemplo para ela e as outras classes derivadas
# copiem, façam da mesma forma q ele, para isso a gente importa o ABC, from abc import ABC, abstractmethod
# e usamos antes do mod, o @abstractmethod, TAMBEM É NECESSARIO APOS A CLASS COLOCAR ENTRE () A palavra ABC
        
    @abstractmethod
    def aplicar_desconto(self):
        pass
    