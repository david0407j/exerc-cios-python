lista_de_dados=[]


return int (tamanho_em_bytes) / (2**10) **2



with open('sample_data/usuario.txt', 'r') as arquivos:
  for linha in arquivos:
      linha =  linha.strip()
      usuario = linha [:15]
      tamanho_em_disco = transformar_em_megabytes (linha [16:])
      lista_de_dados.append((usuario, tamanho_em_disco))



cabecalho = ''' ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
  ''' 
with open('sample_data/relatório.txt"', 'w') as arquivos:
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
   