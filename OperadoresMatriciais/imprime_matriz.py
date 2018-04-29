def imprime_matriz ( matriz ) :

    linhas = len ( matriz )
    colunas = len ( matriz [0] )


    for i in range ( linhas ) :

        for j in range ( colunas ) :

            valor = matriz[i][j]

            print( str (valor) + "  " )

        if ( i < ( linhas - 1 ) ) :
            print("\r")