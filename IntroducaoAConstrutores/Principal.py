import Carro

def main():
    velocidade = (int)(input("Digite o valor da velocidade, em Km/h : "))
    verifica(velocidade)

    velocidade_max = (int)(input("Digite o valor da velocidade máxima, em Km/h : "))
    verifica(velocidade_max)

    modelo = input("Digite o modelo do carro : ")

    ano = (int)(input("Digite o ano do carro : "))
    verifica(ano)

    cor = input("Digite a cor do modelo {} : ".format(modelo))

    carro = Carro(  )


def verifica(ver):
    assert ver > 0


main()
