from Modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pinda = Restaurante('Pindamanhagaba', 'Regional')
restaurante_pinda.alternar_status()
restaurante_pinda.receber_nota('Marcelo', 10)
restaurante_pinda.receber_nota('Rai', 8)
restaurante_pinda.receber_nota('Rai', 2)




def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()