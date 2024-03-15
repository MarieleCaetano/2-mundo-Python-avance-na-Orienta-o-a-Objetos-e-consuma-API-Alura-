from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #super permite q a gente acesse itens de outra classe, nesse caso é
        #o nome e preco da classe itemcardapio
        self.descricao = descricao
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self.preco -= (self.preco * 0.05) # caso eu queira posso sbstituir essa linha por pass, nao
        #dando desconto algum