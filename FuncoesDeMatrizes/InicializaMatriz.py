def criaMatriz ( numLinhas, numColunas ) :
    '''( int, int, valor )
        Cria uma matriz e retorna com o número de linhas ( numLinhas )
        e colunas ( numColunas ) em que cada elemento é igual ao valor dado'''

    # Cria Uma Matriz Vazia
    # Neste Caso é uma lista
    matriz = []

    for i in range ( numLinhas ) :

        linha = []

        for j in range ( numColunas ) :

            valor = ( float ) ( input ( "Digite o elemento da linha {} e coluna {} da matriz : ".format ( i, j ) ) )

            linha.append ( valor )

        matriz.append ( linha )

    return matriz

def leMatriz (  ) :

    lin = int ( input ( "Digite o número de linhas da matriz : " ) )
    col = int ( input ( "Digite o número de colunas da matriz : " ) )

    A = criaMatriz ( lin, col )
    print ( A [0])

leMatriz()