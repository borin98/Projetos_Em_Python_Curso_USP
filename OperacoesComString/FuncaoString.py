def le_string ( lista_de_string ) :

    min = len( lista_de_string[0] )
    posicao_min = 0

    for i in range ( len ( lista_de_string ) ) :

        if ( min > len ( lista_de_string[i] ) ) :

            min = len( lista_de_string[i] )
            posicao_min = i


    return lista_de_string[ posicao_min ]