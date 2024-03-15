from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super(). __init__(nome, preco)
        self.tamanho = tamanho
    
    def __str__(self):
        return self.nome
    
    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.08) # caso eu queira posso sbstituir essa linha por pass, nao
        #dando desconto algum