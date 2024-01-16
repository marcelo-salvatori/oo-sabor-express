from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante: 
    restaurantes = []

    def __init__(self, nome, categoria) -> None: 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        self._cardapio = []

    def __str__(self) -> str:
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls) -> None:
        cabecalho = f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status'
        linha = f'-' * len(cabecalho)
        print(cabecalho)
        print(linha)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_notas).ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self) -> str:
        return f'✅' if self._ativo else '❌'
    
    def alternar_status(self) -> None:
        self._ativo = not self._ativo
    
    def receber_nota(self, cliente, nota) -> None:
        avaliacao = Avaliacao(cliente, nota)
        if self.nota_valida(nota) and self._ativo:
            self._avaliacao.append(avaliacao)
        else:
            print('A nota digitada é inválida ou o restaurante está inativo. Tente novamente...')
    
    def nota_valida(self, nota) -> bool:
        if 0 < nota <=5:
            return True
        else:
            return False
    
    @property
    def media_notas(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
    
        return round(soma_das_notas / quantidade_de_notas, 2)

    def adicionar_item_no_cardapio(self, item) -> None:
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self) -> None:
        print(f'cardápio do restaurante {self._nome}')
        for i,item in enumerate(self._cardapio,start=1):
            mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}' if hasattr(item,'_descricao') else f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho} ml'
            print(mensagem)

