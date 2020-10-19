#https://colab.research.google.com/drive/1wqUZyVogLcz4fwD2cEhkGYUiIZaMu6rR#scrollTo=HV7gj8ltU73E

TREINO ANALISE CARTAO - SALDO AGO/SET/OUT

!pip install pdfplumber

# IMPORTA BIBLIOTECAS NECESSARIOAS PARA A ANALISE PDF

import pdfplumber
from google.colab import drive
import os

drive.mount('/content/gdrive')                                                    # MONTA O ACESSO AO GOOGLE DRIVE

os.getcwd()                                                                       # VERIFICA QUAL PASTA ESTA
os.chdir('/content/gdrive/My Drive/Trilha de Aprendizado/Python/arquivospdf')     # ALTERA O DIRETORIO DO DRIVE
os.getcwd()                                                                       # VERIFICA QUAL PASTA ESTA


pdfcartao = pdfplumber.open('Bradesco_19102020_103701.pdf')                       # ABRE UM ARQUIVO ESPECIFICO E COLOCA NA VARIAVLE PDFCARTAO
print(pdfcartao.pages)                                                            
pagina2 = pdfcartao.pages[1]                                                      # ESCOLHE UMA PAGINA E COLOCA NA VARIAVEL -ESCOLHA DE ACORDO COM VALOR QUE BUSCA
print(pagina2)
texto2 = pagina2.extract_text()                                                   # EXTRAI O TEXTO DA VARIAVEL PAGINA ESCOLHIDA E COLOCA EM UMA VARIAVELL  
print(texto2)
texto2.split('\n')                                                                # SEPARA OS VALORES POR QUEBRA DE PAGINA


saldo = float(texto2.split('\n')[11].split(':')[1].replace('.','').replace(',','.')) # INSTURÇÃO PARA ALCANCAR O VALOR BUSCADO - SALDO  
print('Saldo -->',saldo)

# AUTOMATIZANDO A ANALISE DE PDF PARA VARIOS EXTRATOS

saldosmes = os.listdir()                                                          # CRIA VARIAVEL PARA RECEBER TODOS ARQUIVOS DA PASTA, NESTA PASTA FICARAO OS EXTRATOS GERAIS
saldosmes                                                                         # IMPRIME OS ARQUIVOS  

# AUTOMATIZACAO PARA PERCORRER OS PFDS NA PASTA

soma = 0                                                                              # CRIA A VARIAVEL SOMA PARA ARMAZENAR TOTAL
saldo_lista = []                                                                      # CRIA LISTA PARA ARMAZENAR OS SALDOS SEPARADOS
for saldo in saldosmes:                                                               # CRIA FOR PARA PERCORRER ARQUIVOS 
  relatorio3 = pdfplumber.open(saldo)                                                 # CRIA RELATORIO3 PARA ABRIR O PDF NA ITERAÇÃO DO FOR
  pagina3 = relatorio3.pages[1]                                                       # OAGINA3 RECEBE A PAGINA 1
  texto3 = pagina3.extract_text()                                                     # VARIAVEL TEXTO3 RECEBE OS TEXTOS EXTRAIDOS NA VARIAVEL PAGINA 3
  val = float(texto3.split('\n')[15].split(':')[1].replace('.','').replace(',','.'))  # INSTRUÇÃO PARA LOCALIZAR O SALDO
  soma =soma + val                                                                    # VARIAVEL PARA SOMAR SALDOS DOS PDFS
  saldo_lista.append(val)                                                             # ATUALIZA NA LISTA O VALOR DO SALDO NO FOR
  print("Extrato:",saldo,"Valor:",val)                                                # IMPRIME QUAL O EXTRATO E VALOR NO FOR 
print('-------------------------')                        
print('Valor total somado:',soma)                                                     # IMRPIME O VALOR DA SOMA DOS EXTRATOS   

print("Lista Saldo:",saldo_lista)                                                     # IMPRIME A LISTA

