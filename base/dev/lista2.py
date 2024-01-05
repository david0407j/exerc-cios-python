lista = [] 
for n in range(10):
  numero = float(input('digite um numero  '))
  lista.append (numero)

  lista.reverse()
  print (lista)


lista = []
for _ in range (10):
 numero = float(input('digite um numero:'))
 lista.append(numero) 
    
    
lista.reverse()
print(lista)



lista = [1, 2,'davidson', [] ]
lista.append (10)
print (lista)



lista_de_dados=[]
def transformar_em_megabytes (tamanho_em_bytes:str) -> float: 


 return int (tamanho_em_bytes) / (2**10) **2



with open('sample_data/usuario.txt', 'r') as arquivos:
  for linha in arquivos:
      linha =  linha.strip()
      usuario = linha [:15]
      tamanho_em_disco = transformar_em_megabytes (linha [16:])
      lista_de_dados.append((usuario, tamanho_em_disco))



  tamanho_total_consumido = sum([tamanho for _,tamanho in lista_de_dados])
  media = tamanho_total_consumido  / len(lista_de_dados)
  arquivos.writelines(cabecalho)
  for indice, dados in enumerate(lista_de_dados, start=1):
    usuario, tamanho_em_disco = dados
    arquivos.writelines(
        f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB         '
        f'{tamanho_em_disco/tamanho_total_consumido:>5.2%}\n')
    
    arquivos.writelines('\n')
    arquivos.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    arquivos.writelines(f'Espaço médio ocupado: {media:.2f} MB')