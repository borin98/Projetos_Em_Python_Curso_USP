import sys, time

class InicializadorDeTexto ( object ) :

    def leituraNormal( self, string ) :

        for char in string :

            print(char, end="")
            sys.stdout.flush()
            time.sleep(0.3)

    def leituraAgitada ( self, string ) :

        for i in string :

            print(i, end="")
            sys.stdout.flush()
            time.sleep(0.8)
