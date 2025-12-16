from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_01 = Restaurante('Reiwa', 'Japonês')
bebida_01 = Bebida('Suco de abacaxi',8,'grande')
prato_01 = Prato('Strogonoff', 29, 'O melhor strogonoff da minha rua')

restaurante_01.adicionar_no_cardapio(bebida_01)
restaurante_01.adicionar_no_cardapio(prato_01)

def main():
    restaurante_01.exibir_cardapio

if __name__ == '__main__':
    main()