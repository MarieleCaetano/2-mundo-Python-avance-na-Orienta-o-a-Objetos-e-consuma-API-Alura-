from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome, preco, descricao, tipo, tamanho):
        super().__init__(nome, preco)
        self.descricao = descricao
        self.tipo = tipo
        self.amanho = tamanho
    
    def __str__(self):
        return self.nome

    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.15) 
