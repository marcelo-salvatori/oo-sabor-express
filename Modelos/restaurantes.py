restaurantes = []
class Restaurante: 
    def __init__(self, nome, categoria): 
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça','Gourmet')

Restaurante.listar_restaurantes()