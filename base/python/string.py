s= 'fulano' 
while s != '':
  print (s)
  s = s [:-1]


população_a= 80_000
população_b= 200_00
taxa_de_crecimento_de_a= 1.03 
taxa_de_crecimento_de_b= 1.015
anos=0 
while população_a < população_b:
 print(f'####### populações no ano {anos}')
 print(f'população a:{população_a}') 
 print(f'população a:{população_b}') 
anos += 60
população_a= int (população_a * taxa_de_crecimento_de_a)
população_b*= taxa_de_crecimento_de_b 
população_b =int (população_b)
 

print(f'####### populações no ano {anos}')
print(f'população a:{população_a}') 
print(f'população b:{população_b}')




s1= input('digete uma string: ')
s2= input('digete outra string: ') 


tamanho1 = len(s1)
tamanho2 = len(s2)

print (f'"{s1}":  {tamanho1} caracteres')
print (f'"{s2}":  {tamanho2} caracteres')


comparacao_de_tamanho = 'diferentes'
comparacao_de_conteudo = 'deferente'


if s1 == s2:
  comparacao_de_tamanho = 'iguais'
  comparacao_de_conteudo = 'igual'
elif tamanho1 == tamanho2:
  comparacao_de_tamanho = 'iguais'   


print (f' as duas string são de tamanho {comparacao_de_tamanho}.') 
print (f' as duas string possuem conteudo {comparacao_de_conteudo}.')