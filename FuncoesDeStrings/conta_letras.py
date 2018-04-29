def conta_letras ( frase, contar = "vogais" ) :

    frase = frase.lower ( )

    contador = 0

    if ( contar == "vogais" ) :

        for i in range ( 0, len ( frase ) ) :

            if ( ord ( frase[i] ) == 97 or
                 ord ( frase[i] ) == 101 or
                 ord ( frase[i] ) == 105 or
                 ord ( frase[i] ) == 111 or
                 ord ( frase[i] ) == 117 ) :

                contador += 1

    else :

        for i in range ( 0, len ( frase ) ) :

            if ( ord ( frase[i] ) != 97  and
                 ord ( frase[i] ) != 101 and
                 ord ( frase[i] ) != 105 and
                 ord ( frase[i] ) != 111 and
                 ord ( frase[i] ) != 117 and
                 ord ( frase[i] ) != 32 ) :

                contador += 1

    return contador