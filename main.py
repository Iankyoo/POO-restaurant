from modelos.restaurante import Restaurante

restaurante_01 = Restaurante('Reiwa', 'Japonês')
restaurante_02 = Restaurante('CQsabe', 'Hamburguer')
restaurante_03 = Restaurante('Nestor', 'Pizza')

restaurante_01.alternar_estado()
restaurante_01.receber_avaliacao('Joao', 10)
restaurante_01.receber_avaliacao('Maria', 7)
restaurante_01.receber_avaliacao('Andre', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()