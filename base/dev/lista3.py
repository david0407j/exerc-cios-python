def imprimir_triangulo_de_numero_crescentes(n: int):
  for linha in range(1, n + 1):
    for coluna in range(1, linha + 1):
      print (coluna, end= '   ')
    print ('') 
  

print ('trangulo com 1 ')
imprimir_triangulo_de_numero_crescentes (1)
print ('trangulo com 2 ')
imprimir_triangulo_de_numero_crescentes (2)
print ('trangulo com 3 ')
imprimir_triangulo_de_numero_crescentes (3)