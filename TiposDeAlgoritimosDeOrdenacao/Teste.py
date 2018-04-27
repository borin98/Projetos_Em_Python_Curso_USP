from Ordenacao import Buscadores

bu = Buscadores.Buscadores()

vetor = [1,2,7,4,9,3]

teste = bu.ordenaVetor ( vetor )

busca = bu.buscaBinaria ( teste, 4 )

print(busca)