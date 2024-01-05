palavra = 'cleide' .upper()

print ('Jogo da Forca')
print ('Descubra a palavra')


print ('A palavra é: ', end='')
for letra in palavra:
  print ('_ ', end='') 
    

conjunto_letras_palavra = set(palavra)
conjunto_letras_digitadas = set()
erros = 0 

while (not conjunto_letras_palavra.issubset(conjunto_letras_digitadas )) and erros < 7:
  print ()
  print () 
  letras_digitada = input('digete uma letra: ').upper()
  conjunto_letras_digitadas.add(letras_digitada)
  if letras_digitada in conjunto_letras_palavra:
    print ('A palavra é: ', end='')
    for letra in palavra:
      if letra in conjunto_letras_digitadas:c
      print (f'{letra}', end='')
      
    else:
         print ('_ ', end='')
         
  else:
    
    erros += 1
    print (f'-> Erro {erros} de 6. Tente de novo!') 



  print ()
  print ('letra ja digitas:', conjunto_letras_palavra)


  if erros < 7:
    print ('parabens, você ganhou!')
  else:
    print ('infelizmente você perde!')