def ordenada ( lista ) :

        vetor = [None]*len( lista )

        for i in range ( len ( lista ) ) :

            vetor[i] = lista[i]

        for i in range ( len ( lista ) ) :

            menorElemento = i

            #criando um vetor de tamanho n - 1 para ordenar e trocar os elementos quando precisar
            for j in range ( i + 1, len ( lista ) ) :

                if ( lista [ menorElemento ] > lista [ j ]  ) :

                    menorElemento = j

            #estamos reajjustando os valores dentro do vetor para printar melhor
            vetor[i], vetor[menorElemento] = vetor[menorElemento], vetor[i]

        for i in range ( len ( lista ) ) :

            if ( vetor[i] != lista[i] ) :

                return False

        return True