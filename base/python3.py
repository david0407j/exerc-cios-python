#exercício de numeros

soma = float(input('digite um numero   ' ))
 

for n in range(2,6):
  soma+= float(input('digite um numero  '))
  media = soma/ n 
  print (f' a soma dos numeros e {soma} e a media e {media}')


numero_1= int(input('o numero')) 
numero_2= int(input('o numero')) 
numero_3= int(input('o numero'))
print ('o maior numero e 50')


maximo = float(input('digito um numero:')) 
for _ in range (4) : 
  maximo = max(maximo,  float(input('digito um numero:')))
  print (f' numero máximo encontrado até agora é: {maximo}')


numero= float(input('digito um numero:')) 
soma = 0
for _ in range (5) :
  soma+= numero
  print (f'numero {soma} ') 




  chocolate = (input('digite o seu chocolate preferido: ')).upper()
if chocolate == 'A':
  print ('armago')
elif chocolate == 'B':
  print ('branco')
elif chocolate == 'P':
   print ('preto')
else:
  print ('invalido')

print (f'programa finalizado')
