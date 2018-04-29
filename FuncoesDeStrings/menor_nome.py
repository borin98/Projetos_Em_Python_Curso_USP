def menor_nome ( nomes ) :

    for i in range ( 0, len( nomes ) ) :

        nomes[i] = nomes[i].strip ( )

    menor_palavra = nomes[0]
    menor_indice = 0

    for i in range ( 1, len ( nomes ) ) :

                if ( len ( menor_palavra ) > len ( nomes[i] ) ) :

                 menor_palavra = nomes[i]

    menor_palavra = menor_palavra.capitalize (  )

    return menor_palavra