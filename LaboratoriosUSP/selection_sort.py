def ordena (lista):
    for i in range(len(lista)):

        menorElemento = i

        # criando um vetor de tamanho n - 1 para ordenar e trocar os elementos quando precisar
        for j in range(i + 1, len(lista)):

            if (lista[menorElemento] > lista[j]):

                menorElemento = j

        # estamos reajjustando os valores dentro do vetor para printar melhor
        lista[i], lista[menorElemento] = lista[menorElemento], lista[i]

    return lista