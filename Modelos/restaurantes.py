
class Restaurante: 
    restaurantes = []

    def __init__(self, nome, categoria): 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        cabecalho = f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status'
        linha = f'-' * len(cabecalho)
        print(cabecalho)
        print(linha)
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return f'✅' if self._ativo else '❌'
    
    def alternar_status(self):
        self._ativo = not self._ativo