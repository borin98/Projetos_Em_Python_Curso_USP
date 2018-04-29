from FuncoesTriangulos import tipo_triangulo

a = ( int ) ( input ( "Digite o valor do cateto a : " ) )
b = ( int ) ( input ( "Digite o valor do cateto b : " ) )
c = ( int ) ( input ( "Digite o valor do cateto c : " ) )

triangulo = tipo_triangulo.tipo_triangulo ( a, b, c )

print ( triangulo.a )
print ( triangulo.b )
print ( triangulo.c )
print ( triangulo.perimetro ( ) )