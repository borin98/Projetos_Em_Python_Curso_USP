def soma_matrizes ( m1, m2 ) :

    # Pegando Os Elementos Da Primeira Matriz
    i1 = len ( m1 )
    j1 = len ( m1[0] )

    # Pegando Os Elementos Da Segunda Matriz
    i2 = len ( m2 )
    j2 = len ( m2[0] )

    # Criando Uma Nova Lista Para Criar A Matriz
    matriz = []

    if ( ( i1 == i2 ) and ( j1 == j2 ) ) :

        for i in range( i1 ):

            # Cria uma nova linha na matriz_soma
            matriz.append( [ ] )

            for j in range( j1 ):

                # Somando os elementos que possuem o mesmo índice

                soma = m1[i][j] + m2[i][j]

                matriz[i].append(soma)

        return matriz

    else :

        return False