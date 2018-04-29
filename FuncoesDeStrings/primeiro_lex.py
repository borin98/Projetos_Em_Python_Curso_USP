def primeiro_lex ( palavra ) :

    primeiro = ord ( palavra[0][0] )
    indice_menor = 0

    for i in range ( 0 ,len ( palavra ) ) :

        for j in range ( 0, len ( palavra[i] ) - 1 ) :

            letra =  palavra[i][ j + 1 ]

            if ( primeiro > ord ( letra ) ) :

                primeiro = ord ( letra )
                indice_menor = ( j + 1 )


    return palavra [ indice_menor ]

