def  contar_caracteres (s):

    """ função que conta os carecteres de uma string
    ex:
>>> contar_caracteres('junio')
    j: 1
    u: 1
    n: 1
    i: 1
    o: 1


    contar_caracteres('banana')
    a: 3
    b: 1
    n: 2


     :param s: string a ser contada
     """

    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
         if caracter == caracter_anterior:
          contagem +=1
         else:
          print (f'{caracter_anterior}:{contagem}')
         caracter_anterior = caracter
         contagem = 1

    print (f'{caracter_anterior}:{contagem}')


if __name__ == '__main__':
    contar_caracteres ('junio')
    print()
    contar_caracteres ('banana')




def validar(ip:str) -> bool:
  numeros = ip.split('.')
  if len(numeros) != 4:
    return False 


  for n in numeros:
    if not (0 <= int (n) <= 255):
      return False 
  return True 
     
isp_validos = []
isp_invalidos = []
with open('sample_data/isp.txt', 'r') as arquivos:
  for linha in arquivos:
    ip = linha.strip()
    if validar(ip):
      isp_validos.append(ip)
    else:
      isp_invalidos.append(ip)
    
with open('sample_data/ips_saida.txt', 'w') as arquivos:
  arquivos.writelines('[Endereços validos:]\n')



  for ip in isp_validos:
     arquivos.writelines(f'{ip}\n')




  arquivos.writelines('\n')
  arquivos.writelines('\n')
  arquivos.writelines('[Endereços invalidos:]\n')



  for ip in isp_invalidos:
    arquivos.writelines(f'{ip}\n')