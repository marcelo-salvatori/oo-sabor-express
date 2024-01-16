from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):

    def __init__(self, nome, preco) -> None:
        super().__init__(nome, preco)
        self._gluten = True
        self._lactose = True

    def __str__(self) -> str:
        return f'{super().__str__(), {self._gluten}, {self._lactose}}'
    
    def aplicar_desconto(self) -> None:
        pass

    def sem_glutem(self):
        self._gluten = False
    
    def sem_lactose(self):
        self._lactose = False