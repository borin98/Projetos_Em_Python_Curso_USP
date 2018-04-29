from random import *
def lista_grande ( n ) :

        vetor = [ None ]*n

        for i in range ( n ) :

            vetor [ i ] = randrange ( n )

        return vetor

vetor = lista_grande ( 3 )

print ( vetor )