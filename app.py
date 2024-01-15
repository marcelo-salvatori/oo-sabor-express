from Modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_pinda = Restaurante('Pindamanhagaba', 'Regional')
restaurante_pinda.alternar_status()



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()