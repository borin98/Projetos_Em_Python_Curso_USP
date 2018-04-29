import Recursao, pytest

class Teste ( object ) :

    @pytest.mark.parametrize ( "lista, valor, esperado", [
        # pode colocar os dados que deseja implementar
    ] )
    def testaBuscaBinariaRecursiva(self, lista, valor, esperado) :

        a = Recursao.FuncoesRecursivas()

        assert a.buscaBinariaRecursiva ( lista, valor ) == esperado
