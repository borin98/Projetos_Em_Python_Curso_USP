class TiposDeBuscas ( object ) :

    """recebe parâmetros da forma ( lista, x -> float ) -> booleano"""
    def buscaSequencial ( self, lista, x ) :

        for i in range ( len ( lista ) ) :

            if ( lista[i] == x ) :

                return True

        return False
    """vamos montar um algorítimo de selectSort, logo, iremos ordenar o vetor na ordem crescente"""
    def selectSort ( self , lista ) :

        for i in range ( len ( lista ) ) :

            menorElemento = i

            #criando um vetor de tamanho n - 1 para ordenar e trocar os elementos quando precisar
            for j in range ( i + 1, len ( lista ) ) :

                if ( lista [ menorElemento ] > lista [ j ]  ) :

                    menorElemento = j

            #estamos reajjustando os valores dentro do vetor para printar melhor
            lista[i], lista[menorElemento] = lista[menorElemento], lista[i]

        for i in range ( len ( lista ) ) :

            print(lista[i])

    def bubbleSort(self, lista) :

        for i in range ( len ( lista ), 0, -1 ) :

            for j in range ( 0, i ) :

                if ( lista[ j ] > lista[ j + 1 ] ) :

                    lista[ j ], lista[ j + 1 ] = lista[ j ], lista[ j + 1 ]