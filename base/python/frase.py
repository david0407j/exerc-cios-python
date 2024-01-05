hora = input('quantos você ganha por hora: ')  
mes= input('o trabalho vai ganhar por mes') 
print ( f'o valor toltal que o trabalhador vai receber por e mes 700')



saque = 299
nota_de_100 = notas_de_50 = notas_de_10 = nota_de_5 = nota_de_1 = 0

nota_de_100, saque = divmod (saque, 100)  

nota_de_50, saque = divmod (saque, 50) 

nota_de_10, saque = divmod (saque, 10) 

nota_de_5, saque = divmod (saque, 5) 

nota_de_1, saque = divmod (saque, 1) 

if nota_de_100 > 0:
  print (f'{nota_de_100} nota (s) de 100 ')

if notas_de_50 > 0:
   print (f'{nota_de_50} nota (s) de 50 ') 
  
if nota_de_10 > 0:
   print (f'{nota_de_10} nota (s) de 10 ') 
if nota_de_100 > 0:
   print  (f'{nota_de_5} nota (s) de 5 ') 
   
if nota_de_1  > 0:
  print (f'{nota_de_1} nota (s) de 1 ')


nome = input('digete um nome: ')

def inverte(davidson): 
 return davidson[::-1]
print (inverte("davidson")) 


nome = 'davidson junio de castro'.upper()

nome_invertido_por_letras = ''.join(reversed(nome)) 

nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print (f'nome com letras maiuculo: {nome}')
print (f'nome com letras maiuculo ivertido por letras: { nome_invertido_por_letras} ')
print (f'nome com letras maiuculo ivertido por letras: { nome_invertido_por_palavras } ')