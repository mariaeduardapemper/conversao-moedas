import matplotlib.pyplot as plt


def grafico_barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL(R$)')
    plt.show()

#grafico_barra(l_moedas, l_valores)

def grafico_pizza(l_moedas, l_valores):
    plt.pie(l_valores, labels = l_moedas)
    plt.title('Proporsão em relação ao BRL - Real Brasileiro')
    plt.show()

#grafico_pizza(l_moedas, l_valores)

def grafico_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL(R$)')
    plt.show()

#grafico_dispersao(l_moedas, l_valores)
