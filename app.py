from modelos.restaurantes import Restaurante
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pinda = Restaurante('Pindamanhagaba', 'Regional')
# restaurante_pinda.alternar_status()
# restaurante_pinda.receber_nota('Marcelo', 10)
# restaurante_pinda.receber_nota('Wilder', 5)
# restaurante_pinda.receber_nota('Rai', 3)
# restaurante_praca.receber_nota('Manoel', 2)

prato_paozinho = Prato('Pãozinho com Manteiga', 2.0, 'Pãozinho com manteiga assado na chapa e servido quentinho na hora')
bebida_cafe = Bebida('Café Expresso', 2.50, 50)

restaurante_praca.adicionar_item_no_cardapio(bebida_cafe)
restaurante_praca.adicionar_item_no_cardapio(prato_paozinho)

prato_paozinho.aplicar_desconto()
bebida_cafe.aplicar_desconto()

sobremesa_tiramissu = Sobremesa('Banoff', 15)
sobremesa_tiramissu.sem_glutem()
sobremesa_tiramissu.sem_lactose()

print(vars(sobremesa_tiramissu))

def main():
    # Restaurante.listar_restaurantes()
    print(vars(prato_paozinho))
    print(bebida_cafe)
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()