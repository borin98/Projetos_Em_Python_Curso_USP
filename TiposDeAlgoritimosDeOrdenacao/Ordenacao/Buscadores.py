class Buscadores ( object ) :

    def buscaSequencial(self, vetor, elemento) :

        for i in range ( len ( vetor ) ) :

            if ( vetor[i] == elemento ) :

                return i

        return False

    def bubbleSort(self, vetor ) :

        troca = False

        for i in range ( 0, len(vetor) ) :

            for j in range ( ( i + 1 ) ,len ( vetor ) ) :

                if ( vetor[i] > vetor[ j ] ) :

                    troca = True
                    vetor[j], vetor[i] = vetor[i], vetor[j]

                i = j

            if ( not troca ) :

                return vetor

            else :

                troca = False
                i = 0

    def ordenaVetor(self, vetor ) :

        for i in range ( len ( vetor ) ) :

            for j in range ( ( i + 1 ) ,len ( vetor ) ) :

                if (vetor[i] > vetor[j]):

                    vetor[i], vetor[ j ] = vetor[j], vetor[ i ]

        return vetor

    def buscaBinaria(self, vetor, elemento) :

        esquerda = 0
        direita = len ( vetor ) - 1
        meio = len(vetor)//2

        while ( esquerda < direita ) :

            if ( elemento == vetor[meio] ) :

                return vetor[meio]

            #siginifica que ele está mais para a direita do vetor
            elif ( elemento >= vetor[ meio ] ) :

                meio = (meio + direita)//2
                direita += 1
            #significa que ele está mais para a esquerda do vetor
            else :

                meio = (meio + esquerda)//2
                esquerda += 1

        return False
