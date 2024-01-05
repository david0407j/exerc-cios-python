nota_1= float(input('digetea primeira nota:'))
nota_2= float(input('digetea a segunda nota:')) 
media =(nota_1 + nota_2) / 2 
print (f'sua média foi: {media}') 
if media >= 10:
  print ('aprovação com distinção') 
elif  media >=  7:
    print ('aprovado') 
else:
    print ('reprovado') 



times = (input('clube maior do mundo: '))
if times == 's':
  print ('santos')
elif times == 'b': 
  print ('barcelona')
else:
  print ('ivalido')


print ('finalizado o programa ')




sexo = (input('digetea o sexo, M masculico F femenino I indefenido: ')).upper()
if sexo == 'M':
  print ('masculino')
elif sexo == 'F':
   print ('femenino')
elif sexo == ('i'):
   print ('indefenido')
else: 
  print ('invalido')




print ('finalizando o programa')




while True:
  try:
    numeros = int(input('digite um valor de 0 a 10:  '))
  except ValueError:
    print ('deve ser fornecido um valor inteiro')
  else:
    if 0<= numeros <= 10:
        print (f'numero informado e: {numeros} ')
        break
    else:
         print ('o numero deve estar entre 0 e 10')
