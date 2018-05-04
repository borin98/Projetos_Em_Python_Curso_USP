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

    def somaLista(self, vetor ) :

        tam = len ( vetor ) - 1
        aux = [] * tam

        if ( tam > 0 ) :

            for i in range ( tam ) :

                aux.append ( vetor[i] )
                resto = vetor[tam]

            return resto + self.somaLista ( aux )

        else :

            return vetor[0]

    def imparesEmListas(self, vetor) :

        tam = len(vetor) - 1
        aux = [] * tam
        final = [] * tam
        aux2 = [] * tam

        if ( tam >= 0 ) :

            if ( vetor[ tam ] %2 != 0 ) :

                final.append ( vetor[tam] )

            for i in range ( tam ) :

                aux.append ( vetor[i] )

            aux2.extend ( self.imparesEmListas ( aux ) )
            final.extend ( aux2 )

        return final

    def organizaVetor(self, vetor) :

        tam = len ( vetor ) - 1

        for i in range ( len ( vetor ) ) :

            if ( i < tam/2 ) :
                vetor[i], vetor[tam - i] = vetor[tam - i], vetor[i]

        return vetor

    def incomodam(self, n) :

        if ( n == 1 ) :

            return "um elefante incomoda muita gente"

        else :

            print ( "{} elefantes incomodam muita gente".format ( n ) )
            String = str ( n ) + "elefantes "+ ( "incomodam "*n ) + "muito mais"
            return String
