from time import sleep
from sys import stdout
from FuncoesPrincipais import InicializadorDeTexto

class Janela ( object ) :

    def __init__ ( self, tipoObjeto ) :

         a = tipoObjeto.nomeObjeto()

         for i in range ( 0, 60 ) :

             if ( i == 30 ) :

                 aux = InicializadorDeTexto.InicializadorDeTexto ( )
                 print(" ", end = "")
                 aux.string_teste ( a )
                 print(" ", end = "")

             print ( "|", end="" )
             stdout.flush()
             sleep(0.4)


    def continuacaoDaJanela ( self, a ) :
        

         InicializadorDeTexto.Teste ( a )