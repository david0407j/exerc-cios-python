lista = [] 
for n in range(5):
  numero = float(input('digite um numero  '))
  lista.append (numero)
  print (lista)

lista = []
for _ in range (5):
 numero = float(input('digite um numero:'))
 lista.append(numero) 
  
print(lista)



notas = []  

while True:
 entrada = input('digite um numero:') 

 if entrada =='-1': 
   break 
 notas.append (float(entrada))
tamanho = len(notas) 
print (f'foram lidas (tamanho) notas')
print (' '.join([str (notas) for notas in notas ])) 
notas.reverse() 

for nota in notas:
  print (nota) 

soma= sum(notas)

print (f'somas das notas e: {soma}')  

media = soma / tamanho 
print (f'a media das notas e: {media}') 
print ('nota acima da media ')
print (' '.join([str (nota) for nota in notas if  nota > media ])) 
print (' nota abaixo de 7:')
print (' '.join([str (nota) for nota in notas if nota < 7])) 
print (' encerrando programa de estatística de notas')



salario = [200, 250, 320, 413, 516, 680, 791, 877, 995, 1000, 2000, 3000] 
contagem_de_faixa_salarial = [0] *  9
for salario in salario:
  indece = salario // 100 -2
  indece_maximo = len(contagem_de_faixa_salarial) - 1
  indece = min(indece, indece_maximo)
  contagem_de_faixa_salarial [indece] += 1
print (contagem_de_faixa_salarial)