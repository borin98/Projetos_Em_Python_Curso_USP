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

    def mergeSort(self, vetor ) :

        # caso base da recursão
        if ( len ( vetor ) <= 1 ) :

            return vetor

        # caso geral pra achar o meio do vetor
        meio = len ( vetor ) // 2

        # fazendo a separação dos vetores em outros menores
        direita = self.mergeSort ( vetor[:meio] )
        esquerda = self.mergeSort ( vetor[meio:] )

        return self.mergeSortInterno ( direita, esquerda )

    def mergeSortInterno(self, direita, esquerda) :

        # esses dois primeiros if são os casos base da recursão

        if ( not esquerda ) :

            return direita

        if ( not direita ) :

            return esquerda

        # fazendo o caso da intercalação da nova lista

        if ( esquerda[0] < direita[0] ) :

            return [ esquerda[0] ] + self.mergeSortInterno ( esquerda[1:], direita )

        return [ direita[0] ] + self.mergeSortInterno ( esquerda, direita[1:] )