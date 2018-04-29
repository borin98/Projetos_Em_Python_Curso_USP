class Carro :

    #   Este construtor recebe o próprio objeto para construção
    def __init__(self, modelo, ano, cor, velocidade, velocidade_max ) :

        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.velocidade_max = velocidade_max

    def acelera ( self, nova_velo ) :

        self.velocidade = nova_velo

        if ( self.velocidade > self.velocidade_max ) :

            self.velocidade = self.velocidade_max

        self.imprime ( )

    def imprime( self ) :

        # o carro está parado neste caso
        if ( self.velocidade == 0 ) :

            print ( "Modelo : {} \nCor : {} \nAno : {}".format ( self.modelo, self.cor, self.ano ) )

        elif ( self.velocidade < self.velocidade_max ) :

            print ( "{} {} indo a {} Km/h".format ( self.modelo, self.cor, self.velocidade ) )

        else :

            print ( "{} {} indo muito rápido !!!".format ( self.modelo, self.cor ) )

    def pare ( self ) :

        self.velocidade = 0
        self.imprime ( )
