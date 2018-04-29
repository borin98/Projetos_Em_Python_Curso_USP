class FuncoesRecursivas ( object ) :

    def fatorial ( self, numero ) :

        if numero < 1 :

            return 1

        else :

            return numero * self.fatorial  ( numero - 1 )

    def fibonacci(self, numero ) :

        if ( numero == 0 or numero == 1 ) :

            return numero

        else :

            return self.fibonacci ( numero - 1 ) + self.fibonacci ( numero - 2 )

    def buscaBinariaRecursiva(self, lista, elemento, min = 0, max = None) :

        """inicializando a variável max quando a função é chamada pela
           primeira vez """

        if ( max == None ) :

            max = len ( lista ) - 1

        # significa que ele não encontrou o elemento na lista
        if ( max < min ) :

            return False

        else :

            # fórmula para o caso geral de devolver o índice do meio
            meio = min + ( ( max - min ) // 2 )

        # siginifica que ele está mais para o lado da direita da lista
        if ( lista [ meio ] > elemento ) :

            return self.buscaBinariaRecursiva ( lista, elemento, min, meio - 1 )

        # siginifica que ele está mais para a esquerda do vetor
        elif ( lista [ meio ] < elemento ) :

            return self.buscaBinariaRecursiva ( lista, elemento, meio + 1, max )

        # siginifica que ele encontrou o elemento
        else :

            return meio