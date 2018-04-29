import Musica

"""subclasse do objeto música"""
class Buscador(object):

    def buscaPorTitulo(self, lista, x) :

        for i in range ( len ( lista ) ) :

            if ( lista[i].titulo == x ) :

                return i

        return -1

    def buscaNormal ( self ) :

        playlist = []

        a = ( int ) ( input ( "Digite quantas músicas deseja criar : " ) )

        while ( a < 0 ) :

            print ( "Valor inválido !!!" )
            a = (int)(input("Digite quantas músicas deseja criar : "))

        for i in range ( a ) :

            titulo = input("Digite o título da música "+ str( i + 1 ) +" : " )
            interprete = input("Digite o interprete da música "+ str( i + 1 ) +" : " )
            compositor = input("Digite o compositor da música "+ str( i + 1 ) +" : " )
            ano = ( int ) ( input("Digite o ano da música "+ str( i + 1 ) +" : " ) )

            while ( ano < 0 ) :

                print(" valor inválido !!! ")
                ano = (int)(input("Digite o ano da música " + str(i + 1) + " : ") )

            objetoMusica = Musica.Musica ( titulo, interprete, compositor, ano )
            playlist.insert( i ,objetoMusica )

            busca = input("\nDigite o título da música que deseja buscar em sua playlist : \n")

            resp = self.buscaPorTitulo ( playlist, busca )

            if ( resp == -1 ) :

                print ( "Sua música preferida não está na playlist !!!" )

            else :

                preferida = playlist[ resp ]

                print ( "\nOs dados da sua música preferida são : \n" )

                print ( "Título : {}".format ( preferida.titulo ) )
                print ( "Interprete : {}".format ( preferida.interprete ) )
                print ( "Compositor : {}".format(preferida.compositor) )
                print ( "Ano : {}".format(preferida.ano) )